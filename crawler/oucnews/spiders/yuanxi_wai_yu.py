# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucnews import util
from oucnews.newsspider import NewsSpider


class Spider(NewsSpider):
    """外国语学院

    某些栏目没有抓取
    """

    name = "院系/外语"

    start_urls = [
        "http://222.195.158.203/index.aspx?menuid=5&type=article&lanmuid=9",
        "http://222.195.158.203/index.aspx?menuid=5&type=article&lanmuid=42",
        "http://222.195.158.203/index.aspx?menuid=7&type=article&lanmuid=32",
        "http://222.195.158.203/index.aspx?menuid=38&type=article&lanmuid=113",
        "http://222.195.158.203/index.aspx?menuid=8&type=article&lanmuid=303",
        "http://222.195.158.203/index.aspx?menuid=8&type=article&lanmuid=323",
    ]

    list_extract_scope = "//ul[@class='article_style_1']"
    list_extract_field = {
        'link': ".//@href",
        'category': "//li[@class='uc_lanmu_site_2']/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@class='uc_lanmu_content']"
    item_extract_field = {
        'datetime': ".//div[@class='articleinfor_tishi']/text()[1]",
        'title': ".//div[@class='articleinfor_title']/text()",
        'content': ".//div[@id='Infor_Content']",
    }

    datetime_format = "%Y/%m/%d %H:%M:%S"

    def process_datetime(self, datetime, response):
        i = datetime.index("\xa0")
        return super(Spider, self).process_datetime(datetime[5:i], response)
