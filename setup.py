from setuptools import setup

from trality_simulator import __version__

VERSION = __version__.version
AUTHOR = __version__.author
DATE = __version__.date
MAIL = __version__.mail
WEBSITE = __version__.web

install_requires = []
with open('requirements.txt', 'rt') as requirements:
    for line in requirements:
        install_requires.append(line.strip())


def list_lines(comment):
    for line in comment.strip().split('\n'):
        yield line.strip()


classifier_text = '''
    Development Status :: 5 - Production/Stable
    Intended Audience :: Developers
    Operating System :: OS Independent
    License :: OSI Approved :: GNU General Public License v3 (GPLv3)
    Programming Language :: Python :: 3.9
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Utilities
'''

setup(
    name='trality_simulator',
    python_requires='>3.6.0',
    version=VERSION,
    description=(
        'Trality API syntax helper and backtesting tool'),
    long_description='None yet',
    author=AUTHOR,
    author_email=MAIL,
    url=WEBSITE,
    license='GPLv3',
    packages=[
        'trality_simulator.subcommands', 'trality_simulator.backtest.exchanges',
        'trality_simulator.backtest', 'trality_simulator'],
    test_suite='test',
    entry_points={
        'console_scripts': ['trality = trality_simulator.commands:main']
    },
    install_requires=install_requires,
    classifiers=list(list_lines(classifier_text)),
    keywords='trading'
)
