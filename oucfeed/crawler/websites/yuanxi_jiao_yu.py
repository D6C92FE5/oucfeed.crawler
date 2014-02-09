# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.websites import BaseWebsite


class Website(BaseWebsite):
    """教育系

    一共11个条目，10个指向其它网站的，这是闹哪样啊喂
    注意这个网站使用了<base>标签，相对url的解析需参考其中的url
    """

    name = "院系/教育"

    list_urls = [
        "http://web.ouc.edu.cn/jyx/yxgg/list.htm",
        "http://web.ouc.edu.cn/jyx/xwzx/list.htm",
    ]

    list_extract_scope = ".articlelist2_tbl"
    list_extract_field = {
        'link': "a",
        'datetime': "td td:nth-child(2)",
        'category': "//div[@frag='窗口6']",
        'title': ".//a//text()[last()]",  # 链接里可能包含其他标签
    }

    item_url_pattern = r"http://web\.ouc\.edu\.cn/jyx/.*/page\.htm"

    item_extract_scope = ".vlink"
    item_extract_field = {
        'datetime': "[height='31']",
        'title': ".biaoti",
        'content': "td.article",
    }

    datetime_format = "%Y-%m-%d"

    def process_link(self, link):
        return util.normalize_url(link, "http://web.ouc.edu.cn/jyx/")

    def process_datetime(self, datetime):
        if len(datetime) > 10:
            datetime = datetime[5:15]
        return super(Website, self).process_datetime(datetime)
