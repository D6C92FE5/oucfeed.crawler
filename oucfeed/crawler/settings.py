# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


BOT_NAME = 'oucfeed.crawler'

SPIDER_MODULES = ['oucfeed.crawler.spiders']
NEWSPIDER_MODULE = 'oucfeed.crawler.spiders'

LOG_LEVEL = 'INFO'

DOWNLOAD_TIMEOUT = 30

USER_AGENT = 'oucfeed.crawler/test (https://github.com/D6C92FE5/oucfeed)'

FEED_EXPORTERS = {
    'json': 'oucfeed.crawler.exporters.JsonItemExporter',
    'js': 'oucfeed.crawler.exporters.JavascriptItemExporter',
}

FEED_SERVER = "http://localhost:8080/"
