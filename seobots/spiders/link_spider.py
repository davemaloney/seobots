# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from seobots.items import BrokenLinksItem
from start_requests import start_requests

class LinkSpiderSpider(CrawlSpider):
    name = "link_spider"

    start_requests = start_requests

    def clean_links(self, links):
        for link in links:
            # remove html fragment (#) and query params (?)
            link.fragment = ''
            link.url = link.url.split('#')[0].split('?')[0]
            yield link

    # rule callback
    def parse_item(self, response):
        item = BrokenLinksItem()
        item['url'] = response.url
        item['status'] = response.status
        item['referer'] = response.request.headers['Referer']
        item['link_text'] = response.meta.get('link_text')
        yield item