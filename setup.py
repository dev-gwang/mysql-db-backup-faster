#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mysql-db-backup-faster.
# https://github.com/heynemann/generator-python-package

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2020, gwangil <pki054@naver.com>

from setuptools import setup, find_packages
from mysql_db_backup_faster import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='mysql-db-backup-faster',
    version=__version__,
    description='an incredible python package',
    long_description='''
an incredible python package
''',
    keywords='',
    author='gwangil',
    author_email='pki054@naver.com',
    url='https://github.com/heynemann/generator-python-package',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'loguru',
        'mysqlclient'
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'mysql-db-backup-faster=mysql_db_backup_faster.cli:main',
        ],
    },
    scripts=['script/mysqlbackup']
)
