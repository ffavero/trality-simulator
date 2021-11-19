# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trality_simulator', 'trality_simulator.examples']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.2,<2.0.0', 'pandas>=1.3.3,<2.0.0']

setup_kwargs = {
    'name': 'trality-simulator',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'IrrationalPi',
    'author_email': 'irrationalpi314@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)

