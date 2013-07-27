# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from itertools import islice

from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from oucnews import util
from oucnews.items import NewsItem


class NewsSpider(BaseSpider):

    default_encoding = 'utf-8'

    start_urls = []

    list_extract_scope = ""
    list_extract_field = {}

    item_extract_scope = ""
    item_extract_field = {}

    item_max_count = 3

    datetime_format = ""

    def __init__(self, *a, **kw):
        super(NewsSpider, self).__init__(*a, **kw)
        self.items = {}

    def parse(self, response):
        h = HtmlXPathSelector(response)
        if self.list_extract_scope != "":
            h = h.select(self.list_extract_scope)

        fields = {k: h.select(v).extract()
                  for k, v in self.list_extract_field.iteritems()}

        fields['link'] = [util.normalize_url(x, response.url)
                          for x in fields['link']]
        fields['link'] = self.process_followed_links(fields['link'], response)

        for value in zip(*fields.itervalues()):
            item = NewsItem(zip(fields.iterkeys(), value))
            item['id_'] = self.generate_item_id(item['link'])
            self.items[item['id_']] = item

        for link in fields['link'][:3]:
            yield Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        h = HtmlXPathSelector(response)
        if self.item_extract_scope != "":
            h = h.select(self.item_extract_scope)

        id_ = self.generate_item_id(response.url)
        i = self.items[id_]
        for k in self.item_extract_field:
            i[k] = h.select(self.item_extract_field[k]).extract()[0]

        return self.process_item(i, response)

    def process_followed_links(self, links, response):
        return links

    def generate_item_id(self, url):
        return url

    def process_item(self, item, response):
        for k in item:
            item[k] = getattr(self, 'process_'+k)(item[k].strip(), response)
        return item

    def process_id_(self, id_, response):
        return id_

    def process_link(self, link, response):
        return link

    def process_datetime(self, datetime, response):
        return util.parse_datetime(datetime, self.datetime_format)

    def process_category(self, category, response):
        return "/".join([self.name, category])

    def process_title(self, title, response):
        return title

    def process_content(self, content, response):
        return util.clean_html(util.unwrap_html(content), response.url)
