# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import re
from datetime import datetime
from urlparse import urljoin

import readability
from w3lib.url import safe_url_string


parse_datetime = datetime.strptime


def unwrap_html(html):
    l = html.index(">")
    r = html.rindex("<")
    return html[l+1:r]


def clean_html(html, url=None):
    return readability.Document(html, url=url).summary(True)


def extract_number(string, index):
    return re.findall(r"\d+", string)[index]


def normalize_url(url, base_url=None, encoding='utf-8'):
    if base_url:
        url = urljoin(base_url, url)
    return safe_url_string(url, encoding)
