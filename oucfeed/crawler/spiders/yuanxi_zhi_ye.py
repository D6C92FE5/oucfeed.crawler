# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """职业技术师范学院

    这个网站的列表页有两种，还好基本能用同一组XPath提取
    内容页中看似分类的东西不会变化，不能用
    """

    name = "院系/职业"

    list_urls = [
        "http://www3.ouc.edu.cn/zyjs/more.aspx?Class_id=1",
        "http://www3.ouc.edu.cn/zyjs/more.aspx?Class_id=2",
        "http://www3.ouc.edu.cn/zyjs/pxzy.aspx",
        "http://www3.ouc.edu.cn/zyjs/zzss.aspx",
        "http://www3.ouc.edu.cn/zyjs/sxsx.aspx",
        "http://www3.ouc.edu.cn/zyjs/hdkb.aspx",
        "http://www3.ouc.edu.cn/zyjs/zjyj.aspx",
        "http://www3.ouc.edu.cn/zyjs/xygz.aspx",
        "http://www3.ouc.edu.cn/zyjs/xxxz.aspx",
    ]

    list_extract_scope = "//div[@id='info']"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@width='12%']/text()",
        'category': "//td[@height='30']/a/text() | //span[@class='STYLE1'][1]/text()",
        'title': ".//a/@title",
    }

    item_extract_scope = "//td[@width='684']"
    item_extract_field = {
        'title': ".//span[@id='Titel']/text()",
        'content': ".//td[@class='news_show_content'][1]",
    }

    datetime_format = "%Y-%m-%d"
