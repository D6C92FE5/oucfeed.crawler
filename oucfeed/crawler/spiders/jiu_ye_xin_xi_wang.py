# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """中国海洋大学 大学生就业信息网 新闻通知

    这个网站的内容页虽然有两种样子，但是页面结构相似
    """

    name = "就业信息网"

    list_urls = [
        "http://career.ouc.edu.cn/newsnotice/employmentnews/",
        "http://career.ouc.edu.cn/newsnotice/realtime/",
        "http://career.ouc.edu.cn/newsnotice/worknotice/",
    ]

    list_extract_scope = ".left_channel"
    list_extract_field = {
        'link': "a",
        'category': "//div[@id='location']/a[3]",
        'title': "a",
    }

    item_url_pattern = r"http://career.ouc.edu.cn/newsnotice/\d+/\d+/article_\d+\.shtml"

    item_extract_scope = "#content"
    item_extract_field = {
        'datetime': ".//div[@class='property']/text()[1]",
        'title': "font[size='4'], h1",
        'content': "#fontzoom",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def process_datetime(self, datetime):
        return super(Spider, self).process_datetime(datetime[:19])
