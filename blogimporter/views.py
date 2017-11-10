# -*- coding: utf-8 -*-
import sys
import json
from flask import redirect
from flask import session
from flask import url_for

from blogimporter.http import server, google
from blogimporter.controllers import blogger
from blogimporter.controllers import get_example_snippets
from blogimporter.controllers import login_required


def log(thing):
    sys.stdout.write('\033[38;5;184m{}\033[0m\n'.format(thing))


@server.route('/oauth/callback')
@google.oauth2callback
def google_user_authorized(token, user, **params):
    session.update(token)
    session['user'] = user
    log(json.dumps(dict(session.items()), indent=2))
    return redirect(url_for('dashboard'))


@google.user_loader
def get_google_user_from_session():
    return session.get('user', {})


@server.route('/')
def index():
    return server.template_response('index.html')


@server.route('/import')
@login_required
def dashboard():
    blog_list = blogger.get_blog_list_for_user()
    context = {
        'blog_list': blog_list,
        'user': session['user'],
    }
    log("blog_list:\n{}".format(json.dumps(blog_list, indent=2)))
    return server.template_response('dashboard.html', context)


@server.route('/auth/google')
def google_login():
    options = {
        'redirect_uri': url_for('google_user_authorized', _external=True),
    }
    return redirect(google.login_url(**options))


@server.route('/login')
def login():
    context = {
        'session': dict(session.items())
    }
    return server.template_response('try-login.html', context)


@server.route('/logout')
def logout():
    session.clear()
    return server.template_response('logout.html')


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
