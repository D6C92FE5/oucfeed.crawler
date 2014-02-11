# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from scrapy.http import Request
from scrapy.selector import Selector

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """管理学院

    这个网站有些内容页直接用JS跳转到其他网站的页面
    """

    name = "院系/管理"

    list_urls = [
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=21",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=22",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=23",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=24",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=25",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=58",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=62",
        "http://www2.ouc.edu.cn/glxy/Article/ShowClass.asp?ClassID=70",
    ]

    list_extract_scope = "//table[@width='649'][2]"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@id='time']/text()",
        'category': "//td[@id='list-tittle']/text()",
        'title': ".//a/text()",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/glxy/Article/[\w/]+/\d+/\d+\.html"

    item_extract_scope = ""
    item_extract_field = {
        'title': "//td[@id='content-tittle']/text()",
        'content': "//td[@id='content-content']//td[1]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def parse_item(self, response):
        sel = Selector(response)
        if self.can_parse_response(response) and not sel.xpath('//body'):
            url = sel.xpath("//script[2]/text()").extract()[0][22:-2]
            request = Request(url, callback=self.parse_item, dont_filter=True)
            request.meta['type'] = 'item'
            request.meta['spider'] = self._original_spider
            request.meta['item'] = response.meta.get('item', None)
            return request
        else:
            return super(Spider, self).parse_item(response)
