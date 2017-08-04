# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Page(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field()
    content = scrapy.Field()
    status_code = scrapy.Field()
    status = scrapy.Field()
    response_time = scrapy.Field()
    hash = scrapy.Field()
    last_modified = scrapy.Field()
    title = scrapy.Field()
    title_length = scrapy.Field()
    title_pixel_width = scrapy.Field()
    size = scrapy.Field()
    word_count = scrapy.Field()
    text_ratio = scrapy.Field()
    redirect_URI = scrapy.Field()
    meta_robots = scrapy.Field()
    meta_refresh = scrapy.Field()
    canonical_URL = scrapy.Field()
    meta_description = scrapy.Field()
    meta_description_length = scrapy.Field()
    meta_description_pixel = scrapy.Field()
    meta_keywords = scrapy.Field()
    meta_keywords_length = scrapy.Field()
    h1 = scrapy.Field()
    h1_length = scrapy.Field()
    h1_count = scrapy.Field()
    h2 = scrapy.Field()
    h2_length = scrapy.Field()
    h2_2 = scrapy.Field()
    h2_2_length = scrapy.Field()
    h2_count = scrapy.Field()
    level = scrapy.Field()
    inlinks = scrapy.Field()
    outlinks = scrapy.Field()
    external_outlinks = scrapy.Field()
    referrer = scrapy.Field()


class BrokenLinksItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    status = scrapy.Field()
    referer = scrapy.Field()
    link_text = scrapy.Field()