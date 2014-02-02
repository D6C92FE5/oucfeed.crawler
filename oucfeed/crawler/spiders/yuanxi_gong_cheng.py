# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """工程学院

    这个网站的内容页链接尾部有一些奇怪的东西
    栏目“图片新闻”没有抓取
    党团相关的内容在另一个网站 http://www3.ouc.edu.cn/gongcheng/dangtuan/
    """

    name = "院系/工程"

    start_urls = [
        "http://www3.ouc.edu.cn/gongcheng/EG_DynamicsList.aspx?id=55&parentid=122",
        "http://www3.ouc.edu.cn/gongcheng/EG_DynamicsList.aspx?id=56&parentid=122",
        "http://www3.ouc.edu.cn/gongcheng/EG_DynamicsList.aspx?id=59&parentid=122",
        "http://www3.ouc.edu.cn/gongcheng/EG_DynamicsList.aspx?id=68&parentid=122",
    ]

    list_extract_scope = "//div[@class='nyrightzi']//li"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@width='14%']/text()",
        'category': "//div[@class='nyrighttopleft']/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@class='nyrightzi']"
    item_extract_field = {
        'category': "//div[@class='nyrighttopleft']/text()",
        'title': ".//div[1]/text()",
        'content': ".//div[2]",
    }

    datetime_format = "%Y-%m-%d"
