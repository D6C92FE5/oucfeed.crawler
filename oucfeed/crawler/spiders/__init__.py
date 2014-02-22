# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from collections import defaultdict

from scrapy.utils.misc import walk_modules

from oucfeed.crawler import util
from oucfeed.crawler.newsspider import NewsSpider


def iterate_all_newsspiders():
    modules = walk_modules(__name__)[1:]
    for module in modules:
        for website in util.iterate_subclasses_in_module(module, NewsSpider):
            yield website

newsspiders = [Spider() for Spider in iterate_all_newsspiders()]


def get_spider_for_item_url(item_url):
    spiders = _newsspider_domains.get(util.get_domain_from_url(item_url), [])
    targets = (x for x in spiders if x.can_parse_item_of_url(item_url))
    return next(targets, None)

_newsspider_domains = defaultdict(list)
for newsspider in newsspiders:
    _newsspider_domains[newsspider.domain].append(newsspider)
_newsspider_domains = dict(_newsspider_domains)
