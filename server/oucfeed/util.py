# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import json
import hashlib
import base64


def json_sha1_base64(obj):
    s = json.dumps(obj, sort_keys=True)
    h = hashlib.sha1(s).digest()
    b = base64.urlsafe_b64encode(h)
    return b.strip('=')

