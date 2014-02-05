# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime
import json
import urllib2
from urlparse import urljoin

from oucfeed.crawler import settings


def normalize(news):
    news.sort(key=lambda x: x.get('datetime', datetime.min))
    for item in news:
        item['datetime'] = str(item.get('datetime', ""))
    news = map(dict, news)
    return news


def upload(news):
    data = json.dumps(normalize(news))
    url = urljoin(settings.FEED_SERVER, "news")
    headers = {"Content-Type": "application/json"}
    request = urllib2.Request(url, data, headers)
    r = urllib2.urlopen(request)
    if r.code != 200:
        raise urllib2.HTTPError(r.url, r.code, r.msg, None, None)

