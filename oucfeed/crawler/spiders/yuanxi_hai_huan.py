# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋环境学院

    党团相关的内容在另一个网站 http://www2.ouc.edu.cn/cpeo/dangtuan/index.asp
    虽然和这个网站很相似但代码有一些差别，不要用同一个Spider抓取
    """

    name = "院系/海环"

    list_urls = [
        "http://www2.ouc.edu.cn/cpeo/news.asp?cId=1",
        "http://www2.ouc.edu.cn/cpeo/news.asp?cId=2",
    ]

    list_extract_scope = "//table[@width='90%']"
    list_extract_field = {
        'link': ".//a[@class='font1link']/@href",
        'datetime': ".//td[@class='lv2']/text()",
        'category': "//td[@width='80%']//text()",
        'title': ".//a[@class='font1link']/@title",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/cpeo/news-ny\.asp"

    item_extract_scope = "//td[@width='77%']/table"
    item_extract_field = {
        'category': ".//strong[1]//text()",
        'title': ".//strong[2]/text()",
        'content': ".//td[@class='font1'][2]",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category):
        category = category[:-2]
        return super(Spider, self).process_category(category)
