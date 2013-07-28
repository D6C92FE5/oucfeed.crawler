# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


BOT_NAME = 'oucnews'

SPIDER_MODULES = ['oucnews.spiders']
NEWSPIDER_MODULE = 'oucnews.spiders'

LOG_LEVEL = 'INFO'

DOWNLOAD_TIMEOUT = 30

USER_AGENT = 'oucnews/test (https://github.com/D6C92FE5/oucfeed)'

FEED_EXPORTERS = {
    'json': 'oucnews.exporters.JsonItemExporter',
    'js': 'oucnews.exporters.JavascriptItemExporter',
}
