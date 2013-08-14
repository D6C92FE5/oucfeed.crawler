# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import json
import hashlib
import base64
from datetime import datetime

from oucfeed import config


def json_sha1_base64(obj):
    s = json.dumps(obj, sort_keys=True)
    h = hashlib.sha1(s).digest()
    b = base64.urlsafe_b64encode(h)
    return b.strip('=')


def try_parse_int(string, default):
    try:
        ret = int(string)
    except (TypeError, ValueError):
        ret = default
    return ret


def parse_output_count(string):
    ret = try_parse_int(string, config.EXPORT_COUNT_DEFAULT)
    ret = max(ret, config.EXPORT_COUNT_MIN)
    ret = min(ret, config.EXPORT_COUNT_MAX)
    return ret


def parse_datetime(datetime_string):
    return datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
