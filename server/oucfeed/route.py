# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy

from oucfeed import cors

from oucfeed.root import Root
from oucfeed.news import News
from oucfeed.category import Category
from oucfeed.profile import Profile
from oucfeed.feed import Feed


config = {
    '/': {
        'response.headers.Access-Control-Allow-Origin': "*",  # CORS
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.cors.on': True,
    },
}

root = Root()
root.news = News()
root.category = Category()
root.profile = Profile()
root.rss = Feed('rss')
root.atom = Feed('atom')
