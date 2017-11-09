# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from blogimporter.http import root_node


def get_example_snippets():
    result = scan_files()
    return dict(result)


def load_node(node):
    contents = open(node.path).read()
    return node.basename, contents


def scan_files():
    for node in root_node.glob('*.py'):
        yield load_node(node)
