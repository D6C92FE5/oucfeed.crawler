# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """观海听涛

    列表页没有添加全
    """

    name = "观海听涛"

    list_urls = [
        "http://xinwen.ouc.edu.cn/Article/Class3/xwlb/index.html",
        "http://xinwen.ouc.edu.cn/ghttxsz/xyzhzy/ytp/index.html",
        "http://xinwen.ouc.edu.cn/ghttxsz/yxjjzy/xwlb/index.html",
        "http://xinwen.ouc.edu.cn/Article/tzgg/index.html",
        "http://xinwen.ouc.edu.cn/Article/hdyl/index.html",
    ]

    list_extract_scope = ".c_main_one"
    list_extract_field = {
        'link': "a",
        'category': "//div[@class='r_navigation']",
        'title': "a",
    }

    item_url_pattern = r"http://xinwen.ouc.edu.cn/[\w/]+/\d+/\d+/\d+/\d+.html"

    item_extract_scope = "[style='margin-left:3px;margin-right:3px;']"
    item_extract_field = {
        'datetime': ".c_title_author span:nth-child(3)",
        'title': ".biaotiziti",
        'content': ".hang",
    }

    datetime_format = "%Y年%m月%d日"

    def _smart_selector(self, selector, field):
        if field != 'category':
            selector = super(Spider, self)._smart_selector(selector, field)
        return selector

    def process_datetime(self, datetime):
        return super(Spider, self).process_datetime(datetime[5:])

    def process_category(self, category):
        category = util.clear_html_tags(category)
        category = category.replace("\r\n", "").replace(" ", "").replace(">>", "/")
        i = category.index("/") + 1
        return super(Spider, self).process_category(category[i:])

    def process_content(self, content):
        i = content.rindex('<div class="bshare">')
        return content[:i]
