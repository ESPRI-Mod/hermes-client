# -*- coding: utf-8 -*-

"""
.. module:: setup.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Prodiguer client setup.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
import os

from setuptools import setup
from setuptools import find_packages



# List of 3rd party python dependencies.
_REQUIRES = [
    'arrow',
    'requests'
]


def read(*paths):
    """Build a file path from *paths* and return the contents.

    """
    with open(os.path.join(*paths), 'r') as file_:
        return file_.read()


setup(
    name='prodiguer_client',
    version='0.1.0',
    description='prodiguer-client is a python client library for interacting with prodiguer web services.',
    long_description=(read('README.rst')),
    install_requires=_REQUIRES,
    url='https://github.com/Prodiguer/prodiguer-client',
    license='CeCILL',
    author='Mark Anthony Greenslade',
    author_email='momipsl@ipsl.fr',
    packages=find_packages(exclude=['jobs*', 'shell*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)