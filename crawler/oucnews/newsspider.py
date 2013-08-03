# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from itertools import cycle

from scrapy import log
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from oucnews import util
from oucnews.items import NewsItem


class NewsSpider(BaseSpider):

    start_urls = []

    list_extract_scope = ""
    list_extract_field = {}

    item_extract_scope = ""
    item_extract_field = {}

    item_max_count = 5

    datetime_format = ""

    force_response_encoding = None

    def __init__(self, *a, **kw):
        super(NewsSpider, self).__init__(*a, **kw)
        self.items = {}

    def parse(self, response):
        if self.force_response_encoding is not None:
            response._encoding = self.force_response_encoding
            response._cached_ubody = None # 删除解码缓存

        hxs = HtmlXPathSelector(response)
        if self.list_extract_scope != "":
            hxs = hxs.select(self.list_extract_scope)

        fields = {}
        failed = []
        for k, v in self.list_extract_field.iteritems():
            selected = hxs.select(v).extract()
            if len(selected) == 0:
                failed.append(k)
                continue
            selected = [self.process_item_field(k,x,response) for x in selected]
            if k != 'link':  # 数量取 link 的数量，其他项循环填充
                selected = cycle(selected)
            fields[k] = selected
        if failed:
            log.msg("extract 0 item in {} ({})".format(response.url,
                ", ".join(failed)), level=log.WARNING, spider=self)
            return

        # 暂存含有部分信息的项目，在 parse_item 补充完整后再输出
        for value in zip(*fields.itervalues()):
            item = NewsItem(zip(fields.iterkeys(), value))
            self.items[item['link']] = item

        fields['link'] = self.process_followed_links(fields['link'], response)

        for link in fields['link'][:self.item_max_count]:
            yield Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        if self.force_response_encoding is not None:
            response._encoding = self.force_response_encoding
            response._cached_ubody = None # 删除解码缓存

        hxs = HtmlXPathSelector(response)
        if self.item_extract_scope != "":
            hxs = hxs.select(self.item_extract_scope)

        i = self.items[response.url]
        failed = []
        for k, v in self.item_extract_field.iteritems():
            selected = hxs.select(v).extract()
            if len(selected) > 0:
                i[k] = self.process_item_field(k, selected[0], response)
            else:
                failed.append(k)
        if failed:
            log.msg("extract failed in {} ({})".format(response.url,
                ", ".join(failed)), level=log.WARNING, spider=self)

        return i

    def process_followed_links(self, links, response):
        return links

    def process_item_field(self, field, value, response):
        return getattr(self, 'process_'+field)(value.strip(), response)

    def process_link(self, link, response):
        return util.normalize_url(link, response.url)

    def process_datetime(self, datetime, response):
        return util.parse_datetime(datetime, self.datetime_format)

    def process_category(self, category, response):
        return "/".join([self.name, category])

    def process_title(self, title, response):
        return title

    def process_content(self, content, response):
        return util.clean_html(util.unwrap_html(content), response.url)
