# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """信息科学与工程学院

    这个网站列表页的排序半死不活的（或许有隐藏的置顶功能？），只能从首页抓取
    主站和党团网站数据库相通，党团网站首页内容多一点，所以从党团网站抓取
    内容页没写文章分类，而且这个网站有多种分类方式，放弃提取分类信息
    注意列表中有的条目的链接直接链接到其他网站
    """

    name = "院系/信息"

    start_urls = [
        "http://it.ouc.edu.cn/party/Default.aspx",
    ]

    list_extract_scope = "//table[@class='right1_text_wzt']"
    list_extract_field = {
        'link': ".//@href",
        'category': "text()", # 随便选取点东西，值直接有 process_catagory 确定
        'title': ".//@title",
    }

    item_extract_scope = "//table[@height='200px']"
    item_extract_field = {
        'datetime': ".//span[@id='labTime']//text()",
        'title': ".//span[@id='labTitle']//text()",
        'content': ".//span[@id='labContent']",
    }

    datetime_format = "%Y/%m/%d %H:%M:%S"

    item_max_count = 6 * 6 # 每个分类6个，总共6个分类，全部抓取

    def process_category(self, category, response):
        return self.name
