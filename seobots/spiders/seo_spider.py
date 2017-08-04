# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from seobots.items import Page
from seobots.spiders.start_requests import start_requests

class SEOSpider(CrawlSpider):
    name = "seo_spider"

    start_requests = start_requests

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
        item['title_length'] = len(''.join(item['title']))
        # item['title pixel width'] =
        # item['size'] =
        # item['word_count'] =
        # item['text_ratio'] =
        # item['redirect_URI'] =
        item['meta_robots'] = Selector(response).xpath(
            '//meta[@name="robots"]/@content').extract()
        item['meta_refresh'] = Selector(response).xpath(
            '//meta[@name="refresh"]/@content').extract()
        item['canonical_URL'] = Selector(response).xpath(
            '//link[@rel="canonical"]/@content').extract()
        item['meta_description'] = Selector(response).xpath(
            '//meta[@name="description"]/@content').extract()
        item['meta_description_length'] = len(''.join(item['meta_description']))
        # item['meta_description_pixel'] =
        item['meta_keywords'] = Selector(response).xpath(
            '//meta[@name="keywords"]/@content').extract()
        item['meta_keywords_length'] = len(''.join(item['meta_keywords']))
        item['h1'] = Selector(response).xpath('//h1/text()').extract_first()
        item['h1_length'] = len(''.join(item['h1']))
        item['h1_count'] = len(Selector(response).xpath('//h1/text()').extract())
        item['h2'] = Selector(response).xpath('//h2/text()').extract_first()
        item['h2_length'] = len(''.join(item['h2']))
        item['h2_2'] = Selector(response).xpath('//h2/text()')[1].extract()
        item['h2_2_length'] = len(''.join(item['h2_2']))
        item['h2_count'] = len(Selector(response).xpath('//h2/text()').extract())
        item['level'] = response.meta['depth']
        # item['inlinks'] =
        # item['outlinks'] =
        # item['external outlinks'] =
        yield item
