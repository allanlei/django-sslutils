from distutils.core import setup
from setuptools import find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_packages_in(where, **kwargs):
    return [where] + ['%s.%s' % (where, package) for package in find_packages(where=where, **kwargs)]

setup(
    name = 'django-sslutils',
    version = '0.1.1',
    author = 'Allan Lei',
    author_email = 'allanlei@helveticode.com',
    description = 'SSL helpers for Django',
    keywords = 'django ssl',
    url = 'https://github.com/allanlei/django-sslutils',
    packages=find_packages_in('sslutils'),
    install_requires=[
        'django-appconf>=0.5',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)