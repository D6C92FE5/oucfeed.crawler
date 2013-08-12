# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy
from cherrypy import request, response


def cors(origin="*", methods=None, headers=None):

    response.headers["Access-Control-Allow-Origin"] = origin

    if not methods:
        methods = request.headers.get("Access-Control-Request-Method")
    if methods:
        response.headers["Access-Control-Allow-Methods"] = methods

    if not headers:
        headers = request.headers.get("Access-Control-Request-Headers")
    if headers:
        response.headers["Access-Control-Allow-Headers"] = headers

    return request.method == 'OPTIONS'


cherrypy.tools.cors = cherrypy._cptools.HandlerTool(cors)
