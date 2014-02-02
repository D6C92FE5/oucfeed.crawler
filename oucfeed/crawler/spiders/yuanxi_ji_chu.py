# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """基础教学中心

    注意这个网站内容页文章内容不单独在某个标签里
    虽然内容页有日期但在iframe里不方便抓取，所以从列表页抓取时间
    """

    name = "院系/基础"

    start_urls = [
        "http://222.195.158.131/jcjxzx/more1.htm",
        "http://222.195.158.131/jcjxzx/more2.htm",
        "http://222.195.158.131/jcjxzx/more3.htm",
        "http://222.195.158.131/jcjxzx/more4.htm",
        "http://222.195.158.131/jcjxzx/more5.htm",
        "http://222.195.158.131/jcjxzx/more6.htm",
        "http://222.195.158.131/jcjxzx/more7.htm",
        "http://222.195.158.131/jcjxzx/more8.htm",
    ]

    list_extract_scope = "//table[@width='655']"
    list_extract_field = {
        'link': ".//td[@width='550']//@href",
        'datetime': ".//td[@width='100']/text()",
        'category': "//td[@class='style1']//text()",
        'title': ".//td[@width='550']//a/text()",
    }

    item_extract_scope = "//table[@height='244']"
    item_extract_field = {
        'category': ".//td[@class='style1']//text()",
        'title': ".//div[@class='style17']/text()",
        'content': "./tr[2]/td",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category, response):
        category = category.split(">")[1].strip()
        return super(Spider, self).process_category(category, response)
