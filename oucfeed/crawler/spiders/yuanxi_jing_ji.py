# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """经济学院

    这个网站的分类和子分类的ID是并列的
    只有一级分类时 ?cId=分类ID，两级分类时 ?itemId=主分类ID&cId=子分类ID
    后者可以通过直接指定 ?cId=主分类ID 直接访问这个主分类下的全部内容
    同一条目在列表页和内容页的分类可能不同，这种情况取的列表页的分类
    """

    name = "院系/经济"

    list_urls = [
        "http://www2.ouc.edu.cn/jingji/dangtuan.asp?itemId=4&cId=4",
        "http://www2.ouc.edu.cn/jingji/dangtuan.asp?itemId=5&cId=5",
        "http://www2.ouc.edu.cn/jingji/jiaoyu.asp?itemId=6&cId=6",
        "http://www2.ouc.edu.cn/jingji/jiaoyu.asp?itemId=7&cId=7",
        "http://www2.ouc.edu.cn/jingji/jiaoyu.asp?itemId=26&cId=26",
        "http://www2.ouc.edu.cn/jingji/jiaoyu.asp?itemId=27&cId=27",
        "http://www2.ouc.edu.cn/jingji/news.asp?itemId=32&cId=32",
        "http://www2.ouc.edu.cn/jingji/news.asp?itemId=36&cId=36",
        "http://www2.ouc.edu.cn/jingji/news.asp?itemId=56&cId=56",
    ]

    list_extract_scope = "//td[@height='450']"
    list_extract_field = {
        'link': ".//a[@class='font1link']/@href",
        'datetime': ".//td[@width='14%']/text()",
        'category': "//td[@width='27%']/strong[1]/text()",
        'title': ".//a[@class='font1link']/@title",
    }

    item_extract_scope = "//table[@width='95%']"
    item_extract_field = {
        'title': ".//strong//text()",
        'content': "./tr[4]/td",
    }

    datetime_format = "%Y-%m-%d"

    def process_category(self, category):
        category = category.strip(" >")
        return super(Spider, self).process_category(category)
