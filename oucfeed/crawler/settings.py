# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


BOT_NAME = 'oucfeed.crawler'

SPIDER_MODULES = ['oucfeed.crawler.spiders']
NEWSPIDER_MODULE = 'oucfeed.crawler.spiders'

LOG_LEVEL = 'INFO'
LOG_STDOUT = True


DOWNLOAD_DELAY = 0.1
DOWNLOAD_TIMEOUT = 60

TELNETCONSOLE_ENABLED = False

USER_AGENT = 'oucfeed.crawler/test (https://github.com/D6C92FE5/oucfeed)'

ITEM_PIPELINES = {
    'oucfeed.crawler.datastore.DatastorePipeline': 1000,
    'oucfeed.crawler.history.HistoryPipeline': 1000,
}

FEED_EXPORTERS = {
    'json': 'oucfeed.crawler.exporters.JsonItemExporter',
    'js': 'oucfeed.crawler.exporters.JavascriptItemExporter',
}

FEED_SERVER = "http://localhost:8080/"

UPLOAD_TIMEOUT = 60

EXECUTE_INTERVAL = 30 * 60
