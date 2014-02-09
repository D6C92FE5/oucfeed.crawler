# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from collections import defaultdict
from urlparse import urlsplit

from scrapy import log
from scrapy.http import Request
from scrapy.spider import Spider

from oucfeed.crawler import util
from oucfeed.crawler.websites import iterate_all_websites


class WebsiteSpider(Spider):

    name = "WebsiteSpider"

    def __init__(self, *a, **kw):
        super(WebsiteSpider, self).__init__(*a, **kw)

        websites = [Website() for Website in iterate_all_websites()]

        domains = defaultdict(list)
        for website in websites:
            domains[website.domain].append(website)

        self.websites = websites
        self.domains = dict(domains)

    def start_requests(self):
        for website in self.websites:
            for url in website.list_urls:
                yield Request(url, callback=website.parse_list, dont_filter=True)

    def parse(self, response):
        websites = [x for x in self._get_websites(response.url) if x.can_parse_response(response)]
        if not websites:
            log.msg("can't find corresponding Website to URL {}".format(response.url),
                    level=log.WARNING, spider=self)
        for website in websites:
            for item in website.parse_item(response):
                yield item

    def _get_websites(self, url):
        return self.domains.get(util.get_domain_from_url(url)) or []

