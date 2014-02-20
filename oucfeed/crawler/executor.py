# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from inspect import isclass

from twisted.internet import reactor, defer
from scrapy import log
from scrapy.settings import CrawlerSettings
from scrapy.crawler import Crawler
from scrapy.spidermanager import SpiderManager

from oucfeed.crawler import settings, datastore
from oucfeed.crawler.uploader import upload


log.start(loglevel=settings.LOG_LEVEL)
crawler_settings = CrawlerSettings(settings)
spidermanager = SpiderManager.from_settings(crawler_settings)


def setup_output():
    crawler_settings.overrides['FEED_URI'] = 'test.js'
    crawler_settings.overrides['FEED_FORMAT'] = 'js'


def init_spider(spider):
    if isinstance(spider, basestring):
        spider = spidermanager.create(spider)
    elif isclass(spider):
        spider = spider()
    return spider


def init_spiders(spiders):
    if not spiders:
        spiders = spidermanager.list()
    spiders = map(init_spider, spiders)
    return spiders


def start_crawler(spider):
    crawler = Crawler(crawler_settings)
    crawler.crawl(spider)
    return crawler.start()


def crawl_finished(result):
    news = datastore.get_all()
    log.msg("抓取完成，得到 {} 项".format(len(news)), level=log.INFO)
    #upload(news)


def run(spiders=list()):

    setup_output()  # FIXME

    spiders = init_spiders(spiders)
    crawlers = [start_crawler(x) for x in spiders]

    d = defer.DeferredList(crawlers)
    d.addCallback(crawl_finished)
    d.addErrback(lambda result: log.err())
    d.addBoth(lambda result: reactor.stop())

    reactor.run()
