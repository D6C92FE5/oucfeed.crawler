# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """文学与新闻传播学院

    这个网站有不少内容页会用JS跳转到其他网站的页面
    """

    name = "院系/文新"

    start_urls = [
        "http://www2.ouc.edu.cn/wxxw/Mingjia/Index.asp",
        "http://www2.ouc.edu.cn/wxxw/Wenzhang/Index.asp",
        "http://www2.ouc.edu.cn/wxxw/Jiuye/Index.asp",
    ]

    list_extract_scope = "//td[@class='main_tdbg_575'][1]"
    list_extract_field = {
        'link': ".//td//a[2]/@href",
        'category': "//td[@class='main_title_575'][1]//text()",
        'title': ".//td//a[2]/text()",
    }

    item_extract_scope = "//table[@class='center_tdbgall'][1]"
    item_extract_field = {
        'datetime': "./tr[4]/td/text()[last()]",
        'title': ".//td[@width='65%']//text()[last()]",
        'content': ".//td[@id='fontzoom']",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime, response):
        i = datetime.index("时间：") + 3
        return super(Spider, self).process_datetime(datetime[i:], response)

    def process_category(self, category, response):
        category = category.split("-")[0]
        return super(Spider, self).process_category(category, response)
