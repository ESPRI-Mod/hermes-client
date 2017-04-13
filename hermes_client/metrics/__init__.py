# -*- coding: utf-8 -*-

"""
.. module:: hermes_client.metrics.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Hermes client metrics sub-package intializer.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)

"""
__version__ = '0.4.1.0'


from hermes_client.metrics.api_proxy import add
from hermes_client.metrics.api_proxy import add_batch
from hermes_client.metrics.api_proxy import delete
from hermes_client.metrics.api_proxy import fetch
from hermes_client.metrics.api_proxy import fetch_columns
from hermes_client.metrics.api_proxy import fetch_count
from hermes_client.metrics.api_proxy import fetch_file
from hermes_client.metrics.api_proxy import fetch_list
from hermes_client.metrics.api_proxy import fetch_setup
from hermes_client.metrics.api_proxy import rename
from hermes_client.metrics.api_proxy import set_hashes
from hermes_client.metrics.formatter.main import execute as format
