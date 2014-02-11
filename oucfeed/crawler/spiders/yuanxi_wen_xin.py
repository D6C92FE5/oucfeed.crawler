# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from scrapy.http import Request
from scrapy.selector import Selector

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """文学与新闻传播学院

    这个网站有不少内容页会用JS跳转到其他网站的页面
    """

    name = "院系/文新"

    list_urls = [
        "http://www2.ouc.edu.cn/wxxw/Mingjia/Index.asp",
        "http://www2.ouc.edu.cn/wxxw/Wenzhang/Index.asp",
        "http://www2.ouc.edu.cn/wxxw/Jiuye/Index.asp",
    ]

    list_extract_scope = "//td[@class='main_tdbg_575'][1]"
    list_extract_field = {
        'link': ".//td//a[2]/@href",
        'category': "//td[@class='main_title_575'][1]//text()",
        'title': ".//td//a[2]/text()",
    }

    item_url_pattern = r"http://www2.ouc.edu.cn/wxxw/\w+/ShowArticle\.asp"

    item_extract_scope = "//table[@class='center_tdbgall'][1]"
    item_extract_field = {
        'datetime': "./tr[4]/td/text()[last()]",
        'title': ".//td[@width='65%']//text()[last()]",
        'content': ".//td[@id='fontzoom']",
    }

    datetime_format = "%Y-%m-%d"

    def process_datetime(self, datetime):
        i = datetime.index("时间：") + 3
        return super(Spider, self).process_datetime(datetime[i:])

    def process_category(self, category):
        category = category.split("-")[0]
        return super(Spider, self).process_category(category)

    def parse_item(self, response):
        sel = Selector(response)
        if self.can_parse_response(response) and not sel.xpath('//body'):
            url = sel.xpath("//script[1]/text()").extract()[0][22:-2]
            request = Request(url, callback=self.parse_item, dont_filter=True)
            request.meta['type'] = 'item'
            request.meta['spider'] = self._original_spider
            request.meta['item'] = response.meta.get('item', None)
            return request
        else:
            return super(Spider, self).parse_item(response)
