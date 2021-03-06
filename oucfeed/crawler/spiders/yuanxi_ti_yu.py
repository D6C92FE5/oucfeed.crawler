# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """体育系

    这个网站像一个纯静态的网站
    列表页内容不全，应当从首页抓取
    注意有些">>"带有单独的链接，这些链接需要被过滤掉
    有些标题里面有奇怪的东西，需要去除
    """

    name = "院系/体育"

    list_urls = [
        "http://www3.ouc.edu.cn/sport/index.htm",
    ]

    list_extract_scope = "#Layer7"
    list_extract_field = {
        'link': "a",
        'category': ".//td[@height='35']//text()",
        'title': "a ::text",
    }

    item_url_pattern = r"http://www3.ouc.edu.cn/sport/new\d+\.html"

    item_extract_scope = "//td[@height='302']"
    item_extract_field = {
        'datetime': ".//div[@class='style11']/text()",
        #'title': ".//div[@class='style10']",  # 里面可能会套着其他标签，不从这里提取了
        'content': "./table/tr[last()]/td[last()]",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime):
        return super(Spider, self).process_datetime(datetime[6:])

    def process_title(self, title):
        return title.strip(" >")

    def process_item(self, item):
        return item if item['title'] else None
