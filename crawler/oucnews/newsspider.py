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
        hxs = HtmlXPathSelector(response)
        if self.list_extract_scope != "":
            hxs = hxs.select(self.list_extract_scope)

        fields = {}
        for k, v in self.list_extract_field.iteritems():
            selected = hxs.select(v).extract()
            selected = [self.process_item_field(k,x,response) for x in selected]
            if k != 'link':  # 数量取 link 的数量，其他项循环填充
                selected = cycle(selected)
            fields[k] = selected

        # 暂存含有部分信息的项目，在 parse_item 补充完整后再输出
        for value in zip(*fields.itervalues()):
            item = NewsItem(zip(fields.iterkeys(), value))
            item['id_'] = self.generate_item_id(item['link'])
            self.items[item['id_']] = item

        fields['link'] = self.process_followed_links(fields['link'], response)

        for link in fields['link'][:self.item_max_count]:
            yield Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        if self.item_extract_scope != "":
            hxs = hxs.select(self.item_extract_scope)

        id_ = self.generate_item_id(response.url)
        i = self.items[id_]
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

    def generate_item_id(self, url):
        return self.name + util.extract_number(url, -1)

    def process_item_field(self, field, value, response):
        return getattr(self, 'process_'+field)(value.strip(), response)

    def process_id_(self, id_, response):
        return id_

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
