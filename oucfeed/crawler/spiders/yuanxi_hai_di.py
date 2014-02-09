# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋地球科学学院

    注意这个网站列表页有问题，不显示最近的几篇文章，应当从首页抓取
    首页上的栏目“通知公告”包括栏目“新闻动态”之外的栏目的内容
    """

    name = "院系/海地"

    list_urls = [
        "http://211.64.142.77/",
    ]

    list_extract_scope = "//table[@width='353']"
    list_extract_field = {
        'link': ".//@href",
        'title': ".//@title",
    }

    item_extract_scope = "//table[@class='box']"
    item_extract_field = {
        'datetime': ".//td[@class='info_text']//text()",
        'category': "//td[@class='font13']/a[2]/text()",
        'title': ".//h2/text()",
        'content': ".//div[@align='left']",
    }

    item_max_count = 8 + NewsSpider.item_max_count # 抓取“通知公告”中全部内容

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def process_datetime(self, datetime):
        return super(Spider, self).process_datetime(datetime[3:22])
