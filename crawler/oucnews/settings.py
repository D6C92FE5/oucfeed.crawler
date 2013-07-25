# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals


BOT_NAME = 'oucnews'

SPIDER_MODULES = ['oucnews.spiders']
NEWSPIDER_MODULE = 'oucnews.spiders'

#USER_AGENT = 'oucnews (+http://www.yourdomain.com)'

FEED_EXPORTERS = {
    'json': 'oucnews.exporters.JsonItemExporter',
}
