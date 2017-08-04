# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from seobots.items import Page

import urllib2

class SEOSpider(CrawlSpider):
    # Setting up the CrawlSpider
    name = "seo_spider"

    # urllib2 is sync however we're only using these methods once to initialize the crawler.
    @staticmethod
    def remote_file_to_array(url):
        # read, split, filter, return all non-empty lines
        return filter(None, urllib2.urlopen(url).read().splitlines())

    @staticmethod
    def sitemap_to_array(url):
        results = []
        body = urllib2.urlopen(url).read()
        sitemap = Sitemap(body)
        for item in sitemap:
            results.append(item['loc'])
        return results

    # __init__ is called to get the spider name so avoid doing any extra work
    # in init such as downloading files.
    #
    # args are automatically made available to the spider.

    def start_requests(self):
        # update rules
        # load target domain and then use it once to define the rules
        # target domain is a string value.
        allowed_domains = self.domain
        print 'Target domain: ', allowed_domains

        # If a link matches multiple rules, the first rule wins.
        self.rules = (
            # If a link is within the target domain, follow it.
            Rule(LinkExtractor(allow_domains=[allowed_domains], unique=True),
                 callback='parse_item',
                 process_links='clean_links',
                 follow=True),
            # Crawl external links and don't follow them
            # Rule(LinkExtractor(unique=True),
            #     callback='parse_item',
            #     process_links='clean_links',
            #     follow=False),
        )
        self._compile_rules()

        # now deal with requests
        start_urls = []
        if self.startpage.endswith('.xml'):
            print 'Sitemap detected!'
            start_urls = self.sitemap_to_array(self.startpage)
        elif self.startpage.endswith('.txt'):
            print 'Remote url list detected!'
            start_urls = self.remote_file_to_array(self.startpage)
        else: # single url
            start_urls = [self.startpage]
        print 'Start url count: ', len(start_urls)
        first_url = start_urls[0]
        print 'First url: ', first_url

        # must set dont_filter on the start_urls requests otherwise
        # they will not be recorded in the items output because it'll
        # be considered a duplicate url.
        # see https://github.com/scrapy/scrapy/blob/5daa14770b23da250ccfd4329899a1c3f669b1f3/scrapy/spider.py#L65
        for url in start_urls:
            # pass array of dictionaries to set cookies.
            # http://doc.scrapy.org/en/latest/topics/request-response.html#topics-request-response
            yield scrapy.Request(url, dont_filter=True)

    # Parsing every item (page) the spider will crawl
    def parse_item(self, response):
        item = Page()
        item['referrer'] = response.request.headers.get('Referer', None)
        item['address'] = response.url
        item['content'] = response.headers.get('Content-Type')
        item['status_code'] = response.status
        # item['status'] = 
        # item['response_time'] = 
        # item['hash'] = 
        # item['last_modified'] = 
        item['title'] = Selector(response).xpath('//title/text()').extract()
        item['title_length'] = len( ''.join( item['title'] ) )
        # item['title pixel width'] = 
        # item['size'] = 
        # item['word_count'] = 
        # item['text_ratio'] = 
        # item['redirect_URI'] = 
        item['meta_robots'] = Selector(response).xpath('//meta[@name="robots"]/@content').extract()
        item['meta_refresh'] = Selector(response).xpath('//meta[@name="refresh"]/@content').extract()
        item['canonical_URL'] = Selector(response).xpath('//link[@rel="canonical"]/@content').extract()
        item['meta_description'] = Selector(response).xpath('//meta[@name="description"]/@content').extract()
        item['meta_description_length'] = len( ''.join( item['meta_description'] ) )
        # item['meta_description_pixel'] = 
        item['meta_keywords'] = Selector(response).xpath('//meta[@name="keywords"]/@content').extract()
        item['meta_keywords_length'] = len( ''.join( item['meta_keywords'] ) )
        item['h1'] = Selector(response).xpath('//h1/text()').extract_first()
        item['h1_length'] = len( ''.join( item['h1'] ) )
        item['h1_count'] = len( Selector(response).xpath('//h1/text()').extract() )
        item['h2'] = Selector(response).xpath('//h2/text()')[0].extract()
        item['h2_length'] = len( ''.join( item['h2'] ) )
        item['h2_2'] = Selector(response).xpath('//h2/text()')[1].extract()
        item['h2_2_length'] = len( ''.join( item['h2_2'] ) )
        item['h2_count'] = len( Selector(response).xpath('//h2/text()').extract() )
        item['level'] = response.meta['depth']
        # item['inlinks'] = 
        # item['outlinks'] = 
        # item['external outlinks'] = 
        yield item