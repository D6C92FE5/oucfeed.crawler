# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """教务处 新闻通知"""

    name = "教务处"

    list_urls = [
        "http://jwc.ouc.edu.cn:8080/jwwz/index.jsp",
    ]

    list_extract_scope = "//td[@class='td7']"
    list_extract_field = {
        'link': ".//td[@width='65%']//@href",
        'datetime': ".//td[@width='25%']//text()",
        'title': ".//td[@width='65%']//text()",
    }

    item_url_pattern = r"http://jwc.ouc.edu.cn:8080/jwwz/news\.jsp"

    item_extract_scope = "//td[@class='td7']"
    item_extract_field = {
        'datetime': ".//font[last()-1]/text()",
        'category': "//td[@class='td5']/a[3]/text()",
        'title': ".//b/text()",
        'content': ".//td[3]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"
