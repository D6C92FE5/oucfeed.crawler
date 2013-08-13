# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from google.appengine.ext import ndb


__all__ = [
    "get_news", "set_news",
    "get_news_history", "set_news_history",
    "get_category", "set_category",
    "get_profile", "get_profile",
]


class PickleData(ndb.Model):
    data = ndb.PickleProperty()


def _get_data(item, default=None):
    if item:
        return item.data
    else:
        return default


def get_news():
    return _get_data(PickleData.get_by_id(id="news"), [])

def set_news(news):
    PickleData(id="news", data=news).put()


def get_news_history():
    return _get_data(PickleData.get_by_id(id="news_history"), set())

def set_news_history(news_history):
    PickleData(id="news_history", data=news_history).put()


def get_category():
    return _get_data(PickleData.get_by_id(id="category"), {})

def set_category(category):
    PickleData(id="category", data=category).put()


def get_profile(id_):
    parent = ndb.Key(PickleData, 'profile')
    return _get_data(PickleData.get_by_id(id=id_, parent=parent), {})

def set_profile(id_, profile):
    parent = ndb.Key(PickleData, 'profile')
    PickleData(id=id_, parent=parent, data=profile).put()
