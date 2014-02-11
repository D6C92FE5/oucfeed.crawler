# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """数学科学学院

    这个网站的内容链接结尾有分类ID
    """

    name = "院系/数学"

    list_urls = [
        "http://www2.ouc.edu.cn/math/Ch/NewsList.asp",
    ]

    list_extract_scope = "//td[@width='480']"
    list_extract_field = {
        'link': ".//@href",
        'title': ".//a/text()",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/math/Ch/NewsView\.asp"

    item_extract_scope = "//td[@class='AllCenter']"
    item_extract_field = {
        'datetime': ".//td[@colspan='2'][3]/text()[last()]",
        'category': ".//td[@class='Location']//a[last()]/text()",
        'title': ".//td[@height='40']//text()",
        'content': ".//td[@colspan='2'][5]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def process_datetime(self, datetime):
        l = datetime.index("时间：") + 3
        return super(Spider, self).process_datetime(datetime[l:])
