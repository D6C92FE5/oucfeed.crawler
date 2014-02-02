# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """工程学院 党团委

    这个网站的内容页链接尾部有一些奇怪的东西
    只抓取了党团相关的栏目，与工程学院主站重复的栏目没有抓取
    栏目“文件下载”、“精彩瞬间”没有抓取
    """

    name = "院系/工程/党团"

    start_urls = [
        "http://www3.ouc.edu.cn/gongcheng/dangtuan/EG_DynamicsList.aspx?id=151&parentid=126",
        "http://www3.ouc.edu.cn/gongcheng/dangtuan/EG_DynamicsList.aspx?id=152&parentid=126",
        "http://www3.ouc.edu.cn/gongcheng/dangtuan/EG_DynamicsList.aspx?id=127&parentid=126",
        "http://www3.ouc.edu.cn/gongcheng/dangtuan/EG_DynamicsList.aspx?id=128&parentid=126",
    ]

    list_extract_scope = "//div[@class='nyzi']//li"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@width='14%']/text()",
        'category': "//div[@class='nybtnright']/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@class='nyzi']"
    item_extract_field = {
        'category': "//div[@class='nybtnright']/text()",
        'title': ".//div[1]/text()",
        'content': ".//div[2]",
    }

    datetime_format = "%Y-%m-%d"
