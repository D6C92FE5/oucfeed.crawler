# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋环境学院

    访问不存在的 cId 对应的列表页貌似可以获得全部分类的内容
    """

    name = "院系/海环"

    start_urls = [
        "http://www2.ouc.edu.cn/cpeo/news.asp?cId=0",
        "http://www2.ouc.edu.cn/cpeo/dangtuan/news.asp?cId=0",
    ]

    list_extract_scope = ""
    list_extract_field = {
        'link': "//td[@class='font1'][@width='85%']//@href",
        'datetime': "//td[@class='lv2']/text()",
    }

    item_extract_scope = "//td[@width='77%']/table"
    item_extract_field = {
        'category': ".//strong[1]//text()",
        'title': ".//strong[2]/text()",
        'content': ".//td[@class='font1'][2]",
    }

    datetime_format = "%Y-%m-%d"

    def process_followed_links(self, links, response):
        if "dangtuan" in response.url:
            return [x.replace("ny.asp", "ny1.asp") for x in links]
        else:
            return links

    def process_category(self, category, response):
        ret = [self.name]
        if "dangtuan" in response.url:
            ret.append("党团工作")
        ret.append(category[:-2])
        return "/".join(ret)
