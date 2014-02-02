# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """艺术系

    注意这个网站内容页文章内容不单独在某个标签里
    虽然内容页有日期但在iframe里不方便抓取，所以从列表页抓取时间
    部分栏目没有抓取
    这个网站有大量条目直接链接到其它网站
    """

    name = "院系/艺术"

    start_urls = [
        "http://222.195.158.131/wanb/more1.htm",
        "http://222.195.158.131/wanb/more3.htm",
        "http://222.195.158.131/wanb/more4.htm",
        "http://222.195.158.131/wanb/more7.htm",
        "http://222.195.158.131/wanb/more8.htm",
        "http://222.195.158.131/wanb/more9.htm",
        "http://222.195.158.131/wanb/more10.htm",
        "http://222.195.158.131/wanb/more11.htm",
        "http://222.195.158.131/wanb/more13.htm",
    ]

    list_extract_scope = "//table[@width='655']"
    list_extract_field = {
        'link': ".//td[@width='550']//@href",
        'datetime': ".//td[@width='100']/text()",
        'category': "//td[@class='style1']//text()",
        'title': ".//td[@width='550']//a/text()",
    }

    item_extract_scope = "//table[@height='596']"
    item_extract_field = {
        'category': ".//td[@class='style1']//text()",
        'title': ".//div[@class='style17']/text()",
        'content': "./tr[2]/td",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category, response):
        category = category.split(">")[1].strip()
        return super(Spider, self).process_category(category, response)
