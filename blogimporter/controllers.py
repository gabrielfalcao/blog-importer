import requests
import functools
from flask import redirect
from flask import session
from flask import url_for

from blogimporter.http import root_node


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        if 'access_token' not in session:
            return redirect(url_for('login'))

        return func(*args, **kw)

    return wrapper


def get_example_snippets():
    result = scan_files()
    return dict(result)


def load_node(node):
    contents = open(node.path).read()
    return node.basename, contents


def scan_files():
    for node in root_node.glob('*.py'):
        if node.basename.startswith('__'):
            continue

        yield load_node(node)


def get_google_user_from_session():
    return session.get('user', {})


def get_google_user_id_from_session():
    user = get_google_user_from_session()
    return user.get('id')


def get_google_access_token_from_session():
    return session.get('access_token', None)


class api(object):
    @classmethod
    def get(cls, url, **params):
        if 'access_token' not in params:
            params['access_token'] = get_google_access_token_from_session()

        response = requests.get(url, params=params)
        if '/json' not in response.headers['Content-Type']:
            return None

        return response.json()


class blogger(object):
    @classmethod
    def get_blog_list_for_user(cls):
        user = get_google_user_from_session()
        url = 'https://www.googleapis.com/blogger/v3/users/{id}/blogs'.format(**user)
        return api.get(url) or []
