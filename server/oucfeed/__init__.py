#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from oucfeed import config


# GAE 用的 site-packages
if config.GAE:
    import sys
    sys.path.insert(0, 'site-packages')


import cherrypy

from oucfeed import route


app = cherrypy.tree.mount(route.root, "", route.config)

if __name__ == '__main__':
    if not config.GAE:
        cherrypy.engine.start()
        cherrypy.engine.block()
