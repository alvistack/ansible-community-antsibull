# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['antsibull', 'antsibull.cli', 'antsibull.data', 'antsibull.utils']

package_data = \
{'': ['*'], 'antsibull.data': ['debian/*']}

install_requires = \
['antsibull-changelog>=0.14.0',
 'antsibull-core>=1.3.0,<2.0.0',
 'antsibull-docs>=1.0.0,<2.0.0',
 'asyncio-pool',
 'jinja2']

entry_points = \
{'console_scripts': ['antsibull-build = antsibull.cli.antsibull_build:main',
                     'antsibull-lint = antsibull.cli.antsibull_lint:main']}

setup_kwargs = {
    'name': 'antsibull',
    'version': '0.51.2',
    'description': 'Tools for building the Ansible Distribution',
    'author': 'Toshio Kuratomi',
    'author_email': 'a.badger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ansible-community/antsibull',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
