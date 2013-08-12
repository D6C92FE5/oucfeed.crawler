# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from google.appengine.ext import ndb


__all__ = [
    "get_news", "set_news",
    "get_category", "set_category",
    "get_profile", "get_profile",
]


class JsonData(ndb.Model):
    data = ndb.JsonProperty()


def _get_data(item, default=None):
    if item:
        return item.data
    else:
        return default


def get_news():
    return _get_data(JsonData.get_by_id(id="news"), [])

def set_news(news):
    JsonData(id="news", data=news).put()


def get_category():
    return _get_data(JsonData.get_by_id(id="category"), {})

def set_category(news):
    JsonData(id="category", data=news).put()


def get_profile(id_):
    parent = ndb.Key(JsonData, 'profile')
    return _get_data(JsonData.get_by_id(id=id_, parent=parent), {})

def set_profile(id_, profile):
    JsonData(id=id_, parent=ndb.Key(JsonData, 'profile'), data=profile).put()
