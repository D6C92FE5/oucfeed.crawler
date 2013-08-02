# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from scrapy.item import Item, Field


class NewsItem(Item):
    link = Field()
    datetime = Field()
    category = Field()
    title = Field()
    content = Field()
