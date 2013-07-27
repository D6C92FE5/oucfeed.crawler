#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os

from scrapy.cmdline import execute


if os.path.exists("test.json"):
    os.remove("test.json")
execute("scrapy crawl 院系/海生 -o test.json -t json".split())
