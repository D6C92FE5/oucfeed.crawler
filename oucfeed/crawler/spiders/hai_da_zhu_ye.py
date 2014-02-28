# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import re

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


class Spider(NewsSpider):
    """海大主页

    置顶文章比较多，需要多抓取几项
    列表页是脚本生成的，应当直接从返回的脚本里提取
    """

    name = "海大主页"

    list_urls = [
        "http://211.64.142.8/article_js.asp?ClassID=2&IncludeChild=true&ArticleNum=10"
        "&ShowTitle=true&ShowUpdateTime=true&OrderField=UpdateTime&OrderType=desc",
    ]

    list_extract_pattern = r"<a href='(.*?)' title='(.*?)' target='_blank'>"

    item_url_pattern = r"http://211.64.142.8/Article_Show\.asp"

    item_extract_scope = ""
    item_extract_field = {
        'title': ".tdbg_right2[height='50'] b",
        'content': ".tdbg_right[height='260']",
    }

    item_max_count = 10

    datetime_format = "%Y-%m-%d %H:%M:%S"

    response_encoding = 'gbk'

    def __init__(self, *a, **kw):
        super(Spider, self).__init__(*a, **kw)
        self.list_extract_pattern = re.compile(self.list_extract_pattern)

    def _extract_fields(self, scope_selector, field_selectors):
        response = self.current_response
        if response.meta['type'] == 'list':
            links = []
            titles = []
            datetimes = []
            for item in self.list_extract_pattern.findall(response.body_as_unicode()):
                links.append(self.process_link(item[0]))
                info = item[1].split("\\n")
                titles.append(self.process_title(info[0][5:]))
                datetimes.append(self.process_datetime(info[2][5:]))
            yield 'link', links
            yield 'title', titles
            yield 'datetime', datetimes
        else:
            for field, values in super(Spider, self)._extract_fields(
                    scope_selector, field_selectors):
                yield field, values
