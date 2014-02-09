# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

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

    item_extract_scope = ""
    item_extract_field = {
        'title': "//td[@id='content-tittle']/text()",
        'content': "//td[@id='content-content']//td[1]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"
