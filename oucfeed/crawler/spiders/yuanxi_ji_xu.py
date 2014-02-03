# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """继续教育学院

    这个网站的列表页有一个和其他的不太一样，日期时间那里，看上去很明显
    难以用同一个XPath提取，因此放弃从列表页提取日期时间
    注意这个网站使用了<base>标签，相对url的解析需参考其中的url
    """

    name = "院系/继续"

    start_urls = [
        "http://web.ouc.edu.cn/jxjy/xydt/list.htm",
        "http://web.ouc.edu.cn/jxjy/tzgg/list.htm",
        "http://web.ouc.edu.cn/jxjy/xlzs/list.htm",
        "http://web.ouc.edu.cn/jxjy/pxxm/list.htm",
        "http://web.ouc.edu.cn/jxjy/jxyj/list.htm",
        "http://web.ouc.edu.cn/jxjy/gzzd/list.htm",
        "http://web.ouc.edu.cn/jxjy/zyxz/list.htm",
    ]

    list_extract_scope = "//ul[@id='tpl_w33']"
    list_extract_field = {
        'link': ".//@href",
        #'datetime': ".//div/text()[last()] | .//span[@class=' articlelist1_issuetime ']/text()",
        'category': "//span[@frag='窗口内容'][1]/text()",
        'title': ".//a/text()",
    }

    item_extract_scope = "//div[@frag='窗口内容']"
    item_extract_field = {
        'datetime': ".//span[@class='biaoti12_red'][1]/text()",
        'title': ".//td[@class='biaoti']/text()",
        'content': ".//td[@class='article']",
    }

    datetime_format = "%Y-%m-%d"

    def process_link(self, link, response):
        return util.normalize_url(link, "http://web.ouc.edu.cn/jxjy/")
