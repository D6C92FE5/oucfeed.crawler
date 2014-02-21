# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """研究生招生信息网

    这个网站有二级分类
    """

    name = "研究生招生网"

    list_urls = [
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=3",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=4",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=5",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=9",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=15",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=10",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=20",
        "http://www2.ouc.edu.cn/yzb/Article_Class2.asp?ClassID=22",
    ]

    list_extract_scope = "[width='84%']"
    list_extract_field = {
        'link': "a",
        'category': "//td[@height='5'][1]",
        'title': "a",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/yzb/Article_Show\.asp"

    item_extract_scope = "table[style='border:#cccccc 1px solid;']"
    item_extract_field = {
        'datetime': "td[align='right']",
        'title': ".article_title",
        'content': ".article_content",
    }

    datetime_format = "%Y-%m-%d"

    def _smart_selector(self, selector, field):
        if field != 'category':
            selector = super(Spider, self)._smart_selector(selector, field)
        return selector

    def process_datetime(self, datetime):
        i = datetime.rindex("时间：") + 3
        return super(Spider, self).process_datetime(datetime[i:])

    def process_category(self, category):
        category = util.clear_html_tags(category).replace(" >> ", "/")
        i = category.index("/") + 1
        return super(Spider, self).process_category(category[i:])
