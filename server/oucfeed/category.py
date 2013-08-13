# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

from oucfeed import db


class Category(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        return db.get_category()

    @cherrypy.tools.json_in()
    def POST(self):
        db.set_category(request.json)
        return ""


def add(category_iter):
    category_dict = db.get_category()
    for category in category_iter:
        category_node = category_dict
        for part in category:
            if part not in category_node:
                category_node[part] = {}
            category_node = category_node[part]
    db.set_category(category_dict)


def match(category_dict, category):
    for part in category:
        category_dict = category_dict.get(part)
        if category_dict == {}:
            return True
        if not category_dict:
            break
    return bool(category_dict)