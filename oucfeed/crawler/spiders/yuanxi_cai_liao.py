# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """材料科学与工程研究院

    注意这个网站内容页文章内容不单独在某个标签里
    虽然内容页有日期但在iframe里不方便抓取，所以从列表页抓取时间
    一些栏目没有抓取
    """

    name = "院系/材料"

    list_urls = [
        "http://222.195.158.131/imse/more9.htm",
        "http://222.195.158.131/imse/more16.htm",
        "http://222.195.158.131/imse/more17.htm",
        "http://222.195.158.131/imse/more18.htm",
        "http://222.195.158.131/imse/more20.htm",
        "http://222.195.158.131/imse/more25.htm",
        "http://222.195.158.131/imse/more27.htm",
        "http://222.195.158.131/imse/more28.htm",
    ]

    list_extract_scope = "//table[@width='655']"
    list_extract_field = {
        'link': ".//td[@width='550']//@href",
        'datetime': ".//td[@width='100']/text()",
        'category': "//td[@class='style1']//text()",
        'title': ".//td[@width='550']//a/text()",
    }

    item_url_pattern = r"http://222.195.158.131/imse/\d+\.htm"

    item_extract_scope = "//table[@width='1003']"
    item_extract_field = {
        'category': ".//td[@class='style1']//text()",
        'title': ".//div[@class='style17']/text()",
        'content': "./tr[2]/td",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category):
        category = category.split(">")[1].strip()
        return super(Spider, self).process_category(category)
