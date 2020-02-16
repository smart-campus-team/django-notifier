#!/usr/bin/env python
import django_notifier
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1'

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6"
    "Programming Language :: Python :: 3.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name="django-notifier",
    packages=[
        "django_notifier",
    ],
    install_requires=[
        'pyfcm==1.4.7',
        'Django'
    ],
    author=django_notifier.__author__,
    author_email=django_notifier.__email__,
    classifiers=CLASSIFIERS,
    description="Send push notifications through FCM and APN",
    download_url="https://github.com/smart-campus/django-notifier/tarball/master",
    long_description='',
    url="https://github.com/smart-campus/django-notifier",
    version=VERSION,
)
