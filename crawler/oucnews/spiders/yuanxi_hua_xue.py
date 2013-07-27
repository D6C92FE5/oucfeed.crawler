# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """化学化工学院

    这个网站除栏目“学院通知”之外的新闻栏目多年未更新，因此不进行抓取
    """

    name = "院系/化学"

    start_urls = [
        "http://www2.ouc.edu.cn/chem/ShowClass2.asp?ClassID=13",
    ]

    list_extract_scope = "//td[@height='150']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//font[@color='#999999']/text()",
    }

    item_extract_scope ="//table[@cellpadding='2']"
    item_extract_field = {
        'category': "//td[@width='590']/a[3]/text()",
        'title': ".//strong[1]/text()",
        'content': ".//td[@height='200'][1]",
    }

    datetime_format = "%Y年%m月%d日"
