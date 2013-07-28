# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """医药学院

    此网站的内容页链接尾部有一些奇怪的东西
    党团相关的内容在另一个网站 http://222.195.158.131/yiyaodtgz/
    """

    name = "院系/医药"

    start_urls = [
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%CD%A8%D6%AA%B9%AB%B8%E6",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%D1%A7%D4%BA%D0%C2%CE%C5",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%BF%C6%D1%D0%B6%AF%CC%AC",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%BD%CC%D1%A7%B9%A4%D7%F7",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%D1%A7%CA%F5%BB%E1%D2%E9",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%BA%CF%D7%F7%BD%BB%C1%F7",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%D5%D0%C6%B8%D0%C5%CF%A2",
        "http://www2.ouc.edu.cn/yiyao/newsmore.asp?bigclassname=%D1%D0%BE%BF%B3%C9%B9%FB",
    ]

    list_extract_scope = "//table[@width='650']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@width='15%']/text()",
        'category': "//span[@class='STYLE2']/text()",
    }

    item_extract_scope = "//table[@width='630']"
    item_extract_field = {
        'title': ".//b[1]/text()",
        'content': ".//td[2]",
    }

    datetime_format = "%Y-%m-%d"

    def generate_item_id(self, url):
        return self.name + util.extract_number(url, 1)
