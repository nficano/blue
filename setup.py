#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as fh:
    readme = fh.read()

with open('LICENSE') as fh:
    license = fh.read()

setup(
    name='blue',
    version='0.2.0',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['blue'],
    url='https://github.com/nficano/blue',
    license=license,
    entry_points={
        'console_scripts': [
            'blue = blue.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    description='Bluetooth Toolkit for Python',
    long_description=readme,
    zip_safe=True,
)
