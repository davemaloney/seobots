import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.utils.sitemap import Sitemap

import urllib2

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
