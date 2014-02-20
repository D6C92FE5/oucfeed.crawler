# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import re
from itertools import cycle, islice

from scrapy import log
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import Spider

from oucfeed.crawler import util
from oucfeed.crawler.items import NewsItem


class NewsSpider(Spider):

    domain = ""  # "" -> auto

    list_urls = []

    list_extract_scope = ""
    list_extract_field = {}

    item_max_count = 5

    item_url_pattern = r"^$"

    item_extract_scope = ""
    item_extract_field = {}

    datetime_format = ""

    response_encoding = None  # None -> auto

    def __init__(self, *a, **kw):
        super(NewsSpider, self).__init__(*a, **kw)
        self.items = {}
        self.current_response = None

        if not self.domain and self.list_urls:
            self.domain = util.get_domain_from_url(self.list_urls[0])

        self.list_extract_scope = self._to_xpath_if_css(self.list_extract_scope)
        self.list_extract_field = self._prepare_extract_field(self.list_extract_field)
        self.item_extract_scope = self._to_xpath_if_css(self.item_extract_scope)
        self.item_extract_field = self._prepare_extract_field(self.item_extract_field)

        self.item_url_pattern = re.compile(self.item_url_pattern)

    def start_requests(self):
        for url in self.list_urls:
            request = Request(url, callback=self.parse_list, dont_filter=True)
            request.meta['type'] = 'list'
            request.meta['spider'] = self
            yield request

    def parse_list(self, response):
        self.current_response = response
        self._set_encoding_if_force()

        extracted = dict(self._extract_fields(self.list_extract_scope, self.list_extract_field))
        if 'link' not in extracted:
            return

        for field, values in extracted.iteritems():
            if field != 'link':
                extracted[field] = cycle(values)

        items = (NewsItem(zip(extracted.iterkeys(), values))
                 for values in zip(*extracted.itervalues()))

        items = self.process_items(items)

        # 返回 request
        for item in islice(items, self.item_max_count):
            request = Request(item['link'], callback=self.parse_item, dont_filter=True)
            request.meta['type'] = 'item'
            request.meta['spider'] = self._original_spider
            request.meta['item'] = item
            yield request

    def parse_item(self, response):
        if self.can_parse_response(response):

            self.current_response = response
            self._set_encoding_if_force()

            item = response.meta['item'] or NewsItem()

            extracted = self._extract_fields(self.item_extract_scope, self.item_extract_field)
            for field, values in extracted:
                if not (field == 'category' and 'category' in item):  # category 字段列表值优先
                    item[field] = values[0]

            item['id'] = self.generate_id(item)
            item = self.process_item(item)

            yield item

        else:  # 链接到了其他网站，转交给对应的 Spider 提取

            from oucfeed.crawler.spiders import get_spider_for_response  # 回避循环引用
            spider = get_spider_for_response(response)
            if spider:
                for item in spider.parse_item(response):
                    yield item
            else:
                log.msg("can't find corresponding Spider to URL {}".format(response.url),
                        level=log.WARNING, spider=self._original_spider)

    def _to_xpath_if_css(self, selector):
        if selector and not (selector.startswith("/") or selector.startswith("./")):
            selector = util.css_to_xpath(selector)
        return selector

    def _smart_selector(self, selector, field):
        if not ('/@' in selector or 'text()' in selector):
            if field == 'link':
                selector = '({})/@href'.format(selector)
            elif field != 'content':
                selector = '({})/text()'.format(selector)
        return selector

    def _prepare_extract_field(self, extract_field):
        extract_field = {field: self._smart_selector(self._to_xpath_if_css(selector), field)
                         for field, selector in extract_field.iteritems()}
        return extract_field

    def _set_encoding_if_force(self):
        if self.response_encoding:
            self.current_response._encoding = self.response_encoding
            self.current_response._cached_ubody = None  # 删除解码缓存

    def _extract_fields(self, scope_selector, field_selectors):
        response = self.current_response
        scope = Selector(response).xpath(scope_selector or ".")
        faileds = []
        for field, selector in field_selectors.iteritems():
            values = scope.xpath(selector).extract()
            if len(values) > 0:
                values = [self.process_field(field, x) for x in values]
                yield field, values
            else:
                faileds.append(field)
        if faileds:
            log.msg("extract failed in {} ({})".format(response.url, ", ".join(faileds)),
                    level=log.WARNING, spider=self._original_spider)

    @property
    def _original_spider(self):
        return self.current_response.meta['spider'] if self.current_response else self

    def process_field(self, field, value):
        return getattr(self, 'process_' + field)(value.strip())

    def process_items(self, items):
        return filter(None, (self.process_item(x) for x in items))

    def generate_id(self, item):
        return "/".join([self._original_spider.name, item['link']])

    def can_parse_response(self, response):
        return self.item_url_pattern.match(response.url) is not None

    # 通常可能被重载的方法们 ↓

    def process_link(self, link):
        return util.normalize_url(link, self.current_response.url)

    def process_datetime(self, datetime):
        return util.parse_datetime(datetime, self.datetime_format)

    def process_category(self, category):
        if self._original_spider == self:
            category = "/".join([self.name, category])
        else:
            category = self._original_spider.name
        return category

    def process_title(self, title):
        return title

    def process_content(self, content):
        return util.clean_html(util.unwrap_html(content), self.current_response.url)

    def process_item(self, item):
        return item
