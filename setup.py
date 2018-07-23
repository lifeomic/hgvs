#!/usr/bin/env python

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

requires = [
    'beautifulsoup4==4.4.1',
    'pyfaidx>=0.4.7.1'
]

test_requires = [
    'nose==1.3.7',
    'flake8==3.5.0'
]

setup(
    name='pyhgvs',
    version='0.9.4',
    author='Matt Rasmussen',
    author_email='rasmus@counsyl.com',
    url='https://github.com/counsyl/hgvs/',
    description='HGVS name parsing and formatting',
    long_description=read('README.md'),
    py_modules=('pyhgvs', 'pyhgvs.tests'),
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=requires,
    tests_require=test_requires,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    )
)