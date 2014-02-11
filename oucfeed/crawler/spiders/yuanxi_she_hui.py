# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """社会科学部

    首页上有更精确的日期时间，但没有提取
    """

    name = "院系/社会"

    list_urls = [
        "http://www2.ouc.edu.cn/skb/list.asp?id=1",
        "http://www2.ouc.edu.cn/skb/list.asp?id=1",
        "http://www2.ouc.edu.cn/skb/list.asp?id=3",
        "http://www2.ouc.edu.cn/skb/list.asp?id=9",
        "http://www2.ouc.edu.cn/skb/list.asp?id=10",
        "http://www2.ouc.edu.cn/skb/list.asp?id=13",
        "http://www2.ouc.edu.cn/skb/list.asp?id=15",
    ]

    list_extract_scope = "//div[@class='box2']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//span/text()",
        'category': "//div[@class='tt']/a/text()",
        'title': ".//a/text()",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/skb/show\.asp"

    item_extract_scope = "//div[@id='printBody']"
    item_extract_field = {
        'datetime': "./div[2]//text()",
        'category': "//div[@class='tit']//a[2]/text()",
        'title': ".//h1[1]/text()",
        'content': "./div[3]",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime):
        if len(datetime) > 10:
            datetime = datetime[4:14]
        return super(Spider, self).process_datetime(datetime)
