# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class JiaoWuChuSpider(NewsSpider):

    name = "教务处"

    start_urls = ["http://jwc.ouc.edu.cn:8080/jwwz/index.jsp"]

    followed_urls_scope = "//td[@class='td7']"
    followed_urls_pattern = r"news\.jsp\?news_id=\d+"

    item_extract_scope = "//td[@class='td7']"
    item_extract_field = {
        'datetime': ".//font[last()-1]/text()",
        'category': "//td[@class='td5']/a[3]/text()",
        'title': ".//b/text()",
        'content': ".//td[3]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    def generate_item_id(self, url):
        return self.name + util.extract_number(url, -1)
