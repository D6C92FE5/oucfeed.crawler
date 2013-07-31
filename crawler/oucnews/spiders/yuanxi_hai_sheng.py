# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋生命学院

    这个网站虽然有包含全部分类内容的列表，但不是按时间排序的，必须对每个分类分别抓取
    全站没有按照发布时间排列的列表
    """

    name = "院系/海生"

    start_urls = [
        "http://www2.ouc.edu.cn/hysm/list.asp?class=1",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=3",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=4",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=5",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=6",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=7",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=20",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=21",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=22",
        "http://www2.ouc.edu.cn/hysm/list.asp?class=23",
    ]

    list_extract_scope = "//div[@id='right']//ul[2]"
    list_extract_field = {
        'link': ".//@href",
        'category': "//div[@id='dangqian']//strong/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@id='product']"
    item_extract_field = {
        'datetime': ".//td[1]/text()[2]",
        'category': "//div[@id='dangqian']/a[2]/text()",
        'title': ".//span[1]/text()",
        'content': ".//td[2]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def process_datetime(self, datetime, response):
        i = datetime.index("\t")
        return super(Spider, self).process_datetime(datetime[5:i], response)
