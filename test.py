#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os

from scrapy.cmdline import execute


if os.path.exists("test.js"):
    os.remove("test.js")
execute("scrapy crawl 院系/艺术 -o test.js -t js".split())
