# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """环境科学与工程学院

    注意这个网站内容页文章内容不单独在某个标签里
    虽然内容页有日期但在iframe里不方便抓取，所以从列表页抓取时间
    一些栏目没有抓取，其中有一些列表中链接直接为附件的
    """

    name = "院系/环境"

    start_urls = [
        "http://222.195.158.131/huanjing/more1.htm",
        "http://222.195.158.131/huanjing/more2.htm",
        "http://222.195.158.131/huanjing/more5.htm",
        "http://222.195.158.131/huanjing/more6.htm",
        "http://222.195.158.131/huanjing/more7.htm",
    ]

    list_extract_scope = "//table[@width='655']"
    list_extract_field = {
        'link': ".//td[@width='550']//@href",
        'datetime': ".//td[@width='100']/text()",
        'category': "//td[@class='style1']//text()",
        'title': ".//td[@width='550']//a/text()",
    }

    item_extract_scope = "//table[@height='301']"
    item_extract_field = {
        'category': ".//td[@class='style1']//text()",
        'title': ".//div[@class='style17']/text()",
        'content': "./tr[2]/td",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category, response):
        category = category.split(">")[1].strip()
        return super(Spider, self).process_category(category, response)
