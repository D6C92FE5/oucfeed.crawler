# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from itertools import islice

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from oucnews import util
from oucnews.items import NewsItem


class NewsSpider(CrawlSpider):

    followed_urls_scope = ""
    followed_urls_pattern = r""
    followed_urls_max_count = 3

    item_extract_scope = ""
    item_extract_field = { }

    datetime_format = ""

    def __init__(self, *a, **kw):
        self.rules = (
            Rule(SgmlLinkExtractor(allow=self.followed_urls_pattern,
                                   restrict_xpaths=self.followed_urls_scope),
                 callback='parse_item', follow=True),
        )

        super(NewsSpider, self).__init__(*a, **kw)

    def parse(self, response):
        return islice(super(NewsSpider, self).parse(response),
                      self.followed_urls_max_count)

    def parse_item(self, response):
        h = HtmlXPathSelector(response)
        if self.item_extract_scope != "":
            h = h.select(self.item_extract_scope)

        i = NewsItem()
        for k in self.item_extract_field:
            i[k] = h.select(self.item_extract_field[k]).extract()[0]
        i['id_'] = self.generate_item_id(response.url)
        i['link'] = response.url

        return self.process_item(i, response)

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
