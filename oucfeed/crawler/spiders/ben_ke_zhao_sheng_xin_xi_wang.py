# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """本科招生信息网"""

    name = "本科招生信息网"

    list_urls = [
        "http://www2.ouc.edu.cn/zsb/zsb/Article_List.asp?ClassID=1",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_List.asp?ClassID=4",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_List.asp?ClassID=54",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=8",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=9",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=11",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=10",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=12",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=13",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=14",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=15",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=16",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=17",
        "http://www2.ouc.edu.cn/zsb/zsb/Article_Class2.asp?ClassID=39",
    ]

    list_extract_scope = "table.border_4px"
    list_extract_field = {
        'link': "[valign='top'] > a",
        'category': ".list_title",
        'title': "[valign='top'] > a, [valign='top'] > a font",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/zsb/zsb/Article_Show\.asp"

    item_extract_scope = "table.border_4px"
    item_extract_field = {
        'datetime': ".blue[height='30']",
        'title': ".article_title",
        'content': "[height='150']",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime):
        i = datetime.rindex("时间：") + 3
        return super(Spider, self).process_datetime(datetime[i:].rstrip("\r\n ]"))

    def process_category(self, category):
        return super(Spider, self).process_category(category[:-4])
