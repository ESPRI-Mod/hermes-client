#!/usr/bin/env python

import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'prodiguer_client',
    'prodiguer_client.metrics',
    'prodiguer_client.metrics.formatter',
    'prodiguer_client.ops',
    'prodiguer_client.utils'
]

requires = [
    'arrow',
    'requests'
]

version = ''
with open('prodiguer_client/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='prodiguer_client',
    version=version,
    description='Prodiguer web sercies client side library.',
    long_description=readme,
    author='Mark Anthony Greenslade',
    author_email='momipsl@ipsl.jussieu.fr',
    url='http://es-doc.org',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'prodiguer_client': 'prodiguer_client'},
    include_package_data=True,
    install_requires=requires,
    license='GPL / CeCILL',
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: French',
        'License :: OSI Approved :: CeCILL',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
    extras_require={},
)
