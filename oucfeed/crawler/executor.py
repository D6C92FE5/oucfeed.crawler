# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from inspect import isclass

from twisted.internet import reactor, defer
from scrapy import log
from scrapy.settings import CrawlerSettings
from scrapy.crawler import Crawler
from scrapy.spidermanager import SpiderManager

from oucfeed.crawler import settings, datastore, history
from oucfeed.crawler.uploader import upload


crawler_settings = CrawlerSettings(settings)
log.start_from_settings(crawler_settings)
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
    if upload(news):
        history.dump()
        datastore.clear()


def crawl(spiders):
    deferreds = list(map(start_crawler, init_spiders(spiders)))
    d = defer.DeferredList(deferreds)
    d.addCallback(crawl_finished)
    d.addErrback(lambda result: log.err())
    d.addBoth(lambda result: reactor.callLater(settings.EXECUTE_INTERVAL, crawl, spiders))


def run(spiders=list()):
    history.load()

    if len(spiders) == 1:  # FIXME: Feed exporter 在多个 Spider 同时运行时会把输出混在一起
        setup_output()

    crawl(spiders)

    reactor.run()
