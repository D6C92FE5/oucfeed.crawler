# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import re
from datetime import datetime
from urlparse import urljoin, urlsplit
from inspect import isclass

from lxml.html import defs, make_links_absolute, fragment_fromstring
from lxml.html.clean import Cleaner
from w3lib.url import safe_url_string
from scrapy.selector.csstranslator import ScrapyHTMLTranslator


def encode_if_unicode(string, encoding='utf-8'):
    return string.encode(encoding) if isinstance(string, unicode) else string


def parse_datetime(date_string, format_):
    return datetime.strptime(encode_if_unicode(date_string),
                             encode_if_unicode(format_))


def unwrap_html(html):
    l = html.index(">")
    r = html.rindex("<")
    return html[l+1:r]


def clean_html(html, url=None):
    if html.strip():
        html = html_cleaner.clean_html(html)
        if url is not None:
            html = make_links_absolute(html, url)
    return html
safe_attrs = defs.safe_attrs - {'class', 'align'}
remove_tags = ['font', 'span']
html_cleaner = Cleaner(style=True, page_structure=False,
                       remove_tags=remove_tags, safe_attrs=safe_attrs)


def clear_html_tags(html):
    html = fragment_fromstring(html).text_content()
    return html.strip()


def extract_number(string, index):
    return re.findall(r"\d+", string)[index]


def normalize_url(url, base_url=None, encoding='utf-8'):
    if base_url:
        url = urljoin(base_url, url)
    return safe_url_string(url, encoding)


def get_domain_from_url(url):
    return urlsplit(url).hostname or ""


def iterate_subclasses_in_module(module, base):
    for obj in vars(module).itervalues():
        if isclass(obj) and issubclass(obj, base) and obj.__module__ == module.__name__:
            yield obj


def css_to_xpath(css):
    return _csstranslator.css_to_xpath(css)
_csstranslator = ScrapyHTMLTranslator()
