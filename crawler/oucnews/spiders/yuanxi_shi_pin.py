# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """食品科学与工程学院

    内容页没有写分类，需要从列表页抓取分类信息
    党团相关的内容在另一个网站 http://222.195.158.131/xydw/
    """

    name = "院系/食品"

    start_urls = [
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=5",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=6",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=7",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=8",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=12",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=31",
        "http://www2.ouc.edu.cn/shipin/nylist.asp?id=6&lb1id=73",
    ]

    list_extract_scope = "//table[@width='796'][1]"
    list_extract_field = {
        'link': ".//td/a/@href",
        'category': ".//strong[1]/text()",
    }

    item_extract_scope = "//table[@width='796'][1]"
    item_extract_field = {
        'datetime': ".//td[@width='161']/text()",
        'title': ".//strong[1]/text()",
        'content': ".//table[@width='96%']//tr[2]",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime, response):
        return super(Spider, self).process_datetime(datetime[5:], response)
