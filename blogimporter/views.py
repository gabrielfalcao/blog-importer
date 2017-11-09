# -*- coding: utf-8 -*-

from flask import redirect, url_for, session
from blogimporter.http import server, google
from blogimporter.controllers import get_example_snippets


@server.route('/oauth/callback')
@google.authorized_handler
def authorized(data, *args, **kw):
    access_token = data['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))


@google.tokengetter
def get_access_token():
    return session.get('access_token')


@server.route('/')
def index():
    return server.template_response('index.html')


@server.route('/login')
def login():
    callback = url_for('authorized', _external=True)
    return google.authorize(callback=callback)


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
