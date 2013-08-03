# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """教育系

    一共11个条目，10个指向其它网站的，这是闹哪样啊喂
    注意这个网站使用了<base>标签，相对url的解析需参考其中的url
    """

    name = "院系/教育"

    start_urls = [
        "http://web.ouc.edu.cn/jyx/yxgg/list.htm",
        "http://web.ouc.edu.cn/jyx/xwzx/list.htm",
    ]

    list_extract_scope = "//div[@class='b articlelist2_tbl ']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@height='24']//td[2]/text()",
        'category': "//span[@frag='窗口内容'][1]/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@frag='窗口内容']"
    item_extract_field = {
        'datetime': ".//td[@height='31']/text()[1]",
        'title': ".//td[@class='biaoti']/text()",
        'content': ".//td[@class='article']",
    }

    datetime_format = "%Y-%m-%d"

    def process_link(self, link, response):
        return util.normalize_url(link, "http://web.ouc.edu.cn/jyx/")

    def process_datetime(self, datetime, response):
        if len(datetime) > 10:
            datetime = datetime[5:15]
        return super(Spider, self).process_datetime(datetime, response)
