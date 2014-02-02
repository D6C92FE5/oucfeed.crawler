# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """国际教育学院

    注意这个网站的列表页中的<没有转义，会被识别为标签
    自动检测编码失败，需要手工指定编码
    """

    name = "院系/国际"

    start_urls = [
        "http://www2.ouc.edu.cn/sie/news/WZXW/WZXW.html",
        "http://www2.ouc.edu.cn/sie/news/ZYHNDXM/ZYHNDXM.html",
        "http://www2.ouc.edu.cn/sie/news/JXDT/JXDT.html",
        "http://www2.ouc.edu.cn/sie/news/KCSZ/KCSZ.html",
        "http://www2.ouc.edu.cn/sie/news/KCKH/KCKH.html",
        "http://www2.ouc.edu.cn/sie/news/ZYPG/ZYPG.html",
        "http://www2.ouc.edu.cn/sie/news/JXWJ/JXWJ.html",
        "http://www2.ouc.edu.cn/sie/news/KJXZ/KJXZ.html",
        "http://www2.ouc.edu.cn/sie/news/XGDT/XGDT.html",
        "http://www2.ouc.edu.cn/sie/news/XJGL/XJGL.html",
        "http://www2.ouc.edu.cn/sie/news/BJGL/BJGL.html",
        "http://www2.ouc.edu.cn/sie/news/KQGL/KQGL.html",
        "http://www2.ouc.edu.cn/sie/news/XSZZ/XSZZ.html",
        "http://www2.ouc.edu.cn/sie/news/XZFC/XZFC.html",
        "http://www2.ouc.edu.cn/sie/news/ZSDT/ZSDT.html",
        "http://www2.ouc.edu.cn/sie/news/BMLC/BMLC.html",
        "http://www2.ouc.edu.cn/sie/news/HZYX/HZYX.html",
        "http://www2.ouc.edu.cn/sie/news/TPZS/TPZS.html",
        "http://www2.ouc.edu.cn/sie/news/SPZS/SPZS.html",
        "http://www2.ouc.edu.cn/sie/news/LXWM/LXWM.html",
    ]

    list_extract_scope = "//td[@class='bgm']"
    list_extract_field = {
        'link': ".//td[@width='93%']//@href",
        'category': ".//td[@class='bfont14']/a[last()]/text()",
        'title': ".//td[@width='93%']//a//text()[1]",
    }

    item_extract_scope = "//table[@class='show']"
    item_extract_field = {
        'datetime': ".//td[2]/text()[1]",
        'category': "//td[@class='bfont14']/a[last()]/text()",
        'title': ".//b[1]/text()",
        'content': ".//div[1]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"

    force_response_encoding = 'gb18030'

    def process_datetime(self, datetime, response):
        datetime = "20" + datetime[6:23]
        return super(Spider, self).process_datetime(datetime, response)
