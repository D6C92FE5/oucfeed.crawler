# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """党委研究生工作部

    注意这个网站使用了<base>标签，相对url的解析需参考其中的url
    """

    name = "党委研究生工作部"

    list_urls = [
        "http://web.ouc.edu.cn/ygb/1594/list.htm",
        "http://web.ouc.edu.cn/ygb/1595/list.htm",
        "http://web.ouc.edu.cn/ygb/1605/list.htm",
        "http://web.ouc.edu.cn/ygb/1606/list.htm",
        "http://web.ouc.edu.cn/ygb/1607/list.htm",
        "http://web.ouc.edu.cn/ygb/1608/list.htm",
        "http://web.ouc.edu.cn/ygb/1609/list.htm",
        "http://web.ouc.edu.cn/ygb/1611/list.htm",
        "http://web.ouc.edu.cn/ygb/1612/list.htm",
        "http://web.ouc.edu.cn/ygb/1613/list.htm",
        "http://web.ouc.edu.cn/ygb/1614/list.htm",
        "http://web.ouc.edu.cn/ygb/1615/list.htm",
        "http://web.ouc.edu.cn/ygb/1617/list.htm",
        "http://web.ouc.edu.cn/ygb/1618/list.htm",
        "http://web.ouc.edu.cn/ygb/1619/list.htm",
        "http://web.ouc.edu.cn/ygb/1620/list.htm",
        "http://web.ouc.edu.cn/ygb/1621/list.htm",
    ]

    list_extract_scope = ".listcol"
    list_extract_field = {
        'link': "a",
        'category': "//div[@portletparam='栏目路径']",
        'title': "a",
    }

    item_url_pattern = r"http://web.ouc.edu.cn/ygb/\w+/\w+/\w+/page\.htm"

    item_extract_scope = ".listright"
    item_extract_field = {
        'datetime': ".biaoti12_red:first-child",
        'title': ".atitle",
        'content': ".readbox",
    }

    datetime_format = "%Y-%m-%d"

    def _smart_selector(self, selector, field):
        if field != 'category':
            selector = super(Spider, self)._smart_selector(selector, field)
        return selector

    def process_link(self, link):
        return util.normalize_url(link, "http://web.ouc.edu.cn/ygb/")

    def process_category(self, category):
        category = util.clear_html_tags(category).replace("  ", "/")
        i = category.index("/") + 1
        return super(Spider, self).process_category(category[i:])
