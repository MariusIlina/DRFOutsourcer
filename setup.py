#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='OutSourcer',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='OutSourcer is a place where big companies find contractors and small companies find projects',
    # GETTING-STARTED: set author name (your name):
    author='Your Name',
    # GETTING-STARTED: set author email (your email):
    author_email='marius.ilina@yahoo.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        #'Django==1.8.4',
        #'djangorestframework',
        #'django-cors-headers',
        #'django-haystack',
        #'drf-haystack',
        #'django-filter',
        #'django-redis-cache',
        #'drf-cached-instances',
        #'hiredis==0.1.5',
        #'pysolr'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
