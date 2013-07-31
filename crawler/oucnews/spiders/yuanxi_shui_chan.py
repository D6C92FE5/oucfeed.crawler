# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """水产学院

    栏目数比较多，直接请求了包含所有栏目的页面，减少请求次数，但总抓取数比较多(100+)
    """

    name = "院系/水产"

    start_urls = [
        "http://www2.ouc.edu.cn/shuichan/Article_Class2.asp",
    ]

    list_extract_scope = "//td[@width='440']"
    list_extract_field = {
        'link': ".//@href",
        'title': ".//a/text()",
    }

    item_extract_scope = "//table[@width='930']"
    item_extract_field = {
        'datetime': ".//td[@height='14']/text()[last()]", #last() 中间可能有链接
        'category': ".//font[@color='#FF6600']/text()",
        'title': ".//font[@size='3']/text()",
        'content': ".//span[@class='style11']",
    }

    datetime_format = "%Y-%m-%d"

    item_max_count = 6 * 20 # 每个分类6个，总共20个分类，全部抓取

    def process_datetime(self, datetime, response):
        l = datetime.index("时间：") + 3
        r = datetime.index("    文章")
        return super(Spider, self).process_datetime(datetime[l:r], response)
