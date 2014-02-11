# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """化学化工学院

    一些栏目没有抓取
    """

    name = "院系/化学"

    list_urls = [
        "http://www2.ouc.edu.cn/chem/ShowClass2.asp?ClassID=13",
        "http://www2.ouc.edu.cn/chem/ShowClass2.asp?ClassID=25",
        "http://www2.ouc.edu.cn/chem/ShowClass2.asp?ClassID=26",
    ]

    list_extract_scope = "//td[@height='150']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//font[@color='#999999']/text()",
        'category': "//font[@class='m_tittle']/text()",
        'title': ".//a/text()",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/chem/ShowArticle\.asp"

    item_extract_scope = "//table[@cellpadding='2']"
    item_extract_field = {
        'category': "//td[@width='590']/a[3]/text()",
        'title': ".//strong[1]/text()",
        'content': ".//td[@height='200'][1]",
    }

    datetime_format = "%Y年%m月%d日"
