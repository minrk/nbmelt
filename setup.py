#!/usr/bin/env python

import sys

from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg

with open('nbmelt.py') as f:
    for line in f:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=', 1)[1])
            break


class bdist_egg_disabled(bdist_egg):
    """Disabled version of bdist_egg

    Prevents setup.py install from performing setuptools' default easy_install,
    which it should never ever do.
    """

    def run(self):
        sys.exit("Aborting implicit building of eggs."
                 " Use `pip install .` to install from source.")


data_files = [
    (
        'etc/jupyter/jupyter_notebook_config.d',
        ['nbmelt.json'],
    ),
]


setup_args = dict(
    name="nbmelt",
    version=__version__,
    author="Min Ragan-Kelley",
    author_email="benjaminrk@gmail.com",
    url='http://github.com/minrk/nbmelt',
    description="Shutdown notebooks that don't get used",
    long_description="",
    py_modules=['nbmelt'],
    data_files=data_files,
    license="BSD",
    cmdclass={
        'bdist_egg': bdist_egg if 'bdist_egg' in sys.argv else 'bdist_egg_disabled',
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

setup(**setup_args)
