# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """海洋环境学院

    访问不存在的 cId 对应的列表页貌似可以获得全部分类的内容
    注意iframe，以及内容页存在不带iframe的版本
    列表页本身不带编码信息，需要手动指定
    """

    name = "院系/海环/党团"

    start_urls = [
        "http://www2.ouc.edu.cn/cpeo/dangtuan/news.asp?cId=0",
    ]

    list_extract_scope = ""
    list_extract_field = {
        'link': "//a[@class='font1link']/@href",
        'datetime': "//td[@class='lv2']/text()",
        'title': "//a[@class='font1link']/@title",
    }

    item_extract_scope = "//td[@width='77%']/table"
    item_extract_field = {
        'category': ".//strong[1]//text()",
        'title': ".//strong[2]/text()",
        'content': ".//div[@id='divContent']",
    }

    datetime_format = "%Y-%m-%d"

    force_response_encoding = 'gb18030'

    def process_link(self, link, response):
        link = link.replace("ny.asp", "ny1.asp")
        return util.normalize_url(link, response.url)

    def process_category(self, category, response):
        category = category[:-2]
        return super(Spider, self).process_category(category, response)
