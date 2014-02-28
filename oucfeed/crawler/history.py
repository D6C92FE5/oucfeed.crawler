#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from os import path
from io import open
from datetime import datetime


history_in_file = frozenset()
history = set()


def contains(item_id):
    return item_id in history


def load():
    if path.exists("history"):
        with open("history", encoding='utf-8') as f:
            for line in f:
                if not line.startswith("#"):
                    history.add(line.strip())
        global history_in_file
        history_in_file = frozenset(history)


def dump():
    with open("history", mode='a', encoding='utf-8') as f:
        global history_in_file
        print("#", unicode(datetime.now()), file=f)
        for item_id in history - history_in_file:
            print(item_id, file=f)
        history_in_file = frozenset(history)


class HistoryPipeline(object):
    def process_item(self, item, spider):
        history.add(item['id'])
        return item
