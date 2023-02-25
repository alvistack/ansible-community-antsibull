# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='antsibull',
    version='0.56.1',
    description='Tools for building the Ansible Distribution',
    author_email='Toshio Kuratomi <a.badger@gmail.com>, Felix Fontein <felix@fontein.de>',
    maintainer_email='Felix Fontein <felix@fontein.de>, Maxwell G <maxwell@gtmx.me>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Ansible',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Typing :: Typed',
    ],
    install_requires=[
        'aiofiles',
        'aiohttp>=3.0.0',
        'antsibull-changelog>=0.14.0',
        'antsibull-core<3.0.0,>=1.5.0',
        'asyncio-pool',
        'build',
        'jinja2',
        'packaging>=20.0',
        'semantic-version',
        'sh<2.0.0,>=1.0.0',
        'twiggy',
    ],
    extras_require={
        'codeqa': [
            'flake8>=3.8.0',
            'pylint',
            'reuse',
        ],
        'coverage': [
            'coverage[toml]',
        ],
        'dev': [
            'antsibull[codeqa]',
            'antsibull[coverage]',
            'antsibull[test]',
            'antsibull[typing]',
            'nox',
        ],
        'test': [
            'asynctest',
            'cryptography',
            'pytest',
            'pytest-asyncio>=0.12',
            'pytest-cov',
            'pytest-error-for-skips',
        ],
        'typing': [
            'mypy',
            'pyre-check>=0.9.15',
            'types-aiofiles',
            'types-docutils',
            'types-pyyaml',
        ],
    },
    entry_points={
        'console_scripts': [
            'antsibull-build = antsibull.cli.antsibull_build:main',
        ],
    },
    packages=[
        'antsibull',
        'antsibull.cli',
        'antsibull.data',
        'antsibull.utils',
    ],
    package_dir={'': 'src'},
)
