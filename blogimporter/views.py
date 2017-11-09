# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


from blogimporter.http import server
from blogimporter.controllers import get_example_snippets


@server.route('/')
def index():
    return server.template_response('index.html')


@server.route('/snippets')
def snippets():
    snippets = get_example_snippets()
    context = {
        'snippets': snippets,
    }
    return server.template_response('snippets.html', context)


@server.route('/tufte')
def tufte():
    return server.template_response('tufte.html')
