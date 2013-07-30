# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋环境学院

    访问不存在的 cId 对应的列表页貌似可以获得全部分类的内容
    党团相关的内容在另一个网站 http://www2.ouc.edu.cn/cpeo/dangtuan/index.asp
    虽然和这个网站很相似但代码有一些差别，不要用同一个Spider抓取
    """

    name = "院系/海环"

    start_urls = [
        "http://www2.ouc.edu.cn/cpeo/news.asp?cId=0",
    ]

    list_extract_scope = "//table[@width='90%']"
    list_extract_field = {
        'link': ".//a[@class='font1link']/@href",
        'datetime': ".//td[@class='lv2']/text()",
    }

    item_extract_scope = "//td[@width='77%']/table"
    item_extract_field = {
        'category': ".//strong[1]//text()",
        'title': ".//strong[2]/text()",
        'content': ".//td[@class='font1'][2]",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category, response):
        category = category[:-2]
        return super(Spider, self).process_category(category, response)
