# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import json
import urllib2
from urlparse import urljoin

from oucfeed.crawler import settings


def upload(news):
    url = urljoin(settings.FEED_SERVER, "news")
    headers = {"Content-Type": "application/json"}
    request = urllib2.Request(url, json.dumps(news), headers)
    r = urllib2.urlopen(request)
    if r.code != 200:
        raise urllib2.HTTPError(r.url, r.code, r.msg, None, None)

