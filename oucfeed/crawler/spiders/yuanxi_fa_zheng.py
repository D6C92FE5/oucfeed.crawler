# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """法政学院

    注意这个网站 page.aspx 和 pagestu.aspx 页面的标签id不完全一样
    """

    name = "院系/法政"

    start_urls = [
        "http://www3.ouc.edu.cn/fzxy/xydtmore.aspx?id=1",
        "http://www3.ouc.edu.cn/fzxy/xydtmore.aspx?id=2",
        "http://www3.ouc.edu.cn/fzxy/xydtmore.aspx?id=3",
        "http://www3.ouc.edu.cn/fzxy/xydtmore.aspx?id=4",
        "http://www3.ouc.edu.cn/fzxy/xydtmore.aspx?id=5",
        "http://www3.ouc.edu.cn/fzxy/morestu.aspx?id=2",
        "http://www3.ouc.edu.cn/fzxy/morestu.aspx?id=12",
        "http://www3.ouc.edu.cn/fzxy/morestu.aspx?id=18",
        "http://www3.ouc.edu.cn/fzxy/morestu.aspx?id=19",
        "http://www3.ouc.edu.cn/fzxy/morestu.aspx?id=20",
    ]

    list_extract_scope = "//table[@width='95%'][2]//table"
    list_extract_field = {
        'link': ".//@href",
        'datetime': ".//td[@align='right']/text()",
        'category': "//span[@id='MainContent_Labeltop']//text()",
        'title': ".//a/text()",
    }

    item_extract_scope = ""
    item_extract_field = {
        'datetime': "//span[contains(@id, 'Labeltime')]//text()",
        'title': "//span[contains(@id, 'Labeltitle')]//text()",
        'content': "//span[contains(@id, 'Labelcontent')]",
    }

    datetime_format = "%Y-%m-%d %H:%M:%S"
