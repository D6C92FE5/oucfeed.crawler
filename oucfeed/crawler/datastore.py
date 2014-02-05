# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


data = []


def add(item):
    data.append(item)


def get_all():
    return data


def clear():
    global data
    data = []


class DatastorePipeline(object):
    def process_item(self, item, spider):
        add(item)
        return item
