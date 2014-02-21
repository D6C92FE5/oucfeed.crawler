# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """文科处

    这个网站有二级分类
    """

    name = "文科处"

    list_urls = [
        "http://www2.ouc.edu.cn/wkc/items.asp?cat=A0001",
        "http://www2.ouc.edu.cn/wkc/items.asp?cat=A0002",
        "http://www2.ouc.edu.cn/wkc/items.asp?cat=A0012",
        "http://www2.ouc.edu.cn/wkc/items.asp?cat=A0015",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00090012",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00130006",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00130002",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00130003",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140001",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140002",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140003",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140004",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140005",
        "http://www2.ouc.edu.cn/wkc/itemList.asp?cat=A00140007",
    ]

    list_extract_scope = ".mRight"
    list_extract_field = {
        'link': "span a",
        'category': ".rightTitleSpan",
        'title': "span a",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/wkc/detail\.asp"

    item_extract_scope = ".contentArea"
    item_extract_field = {
        'datetime': ".detailClicks",
        'title': ".detailTitle",
        'content': ".detailInfo",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def process_datetime(self, datetime):
        i = datetime.index(" ")
        return super(Spider, self).process_datetime(datetime[5:i])
