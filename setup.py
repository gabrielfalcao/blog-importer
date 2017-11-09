# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


local_path = lambda *f: abspath(join(dirname(__file__), *f))


def read_requirements():
    lines = open(local_path('requirements.txt')).readlines()
    return list(filter(bool, map(str.strip, lines)))


setup(
    name='blog-importer',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    package_data={
        'blogimporter': ['*.yml'],
    },
    entry_points={
        'console_scripts': ['blog-importer = blogimporter.cli:main'],
    },
)
