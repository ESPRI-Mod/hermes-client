# -*- coding: utf-8 -*-

"""
.. module:: hermes_client.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Hermes client intializer.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)

"""

__title__ = 'hermes_client'
__version__ = '0.4.0.0'
__author__ = 'Mark Anthony Conway-Greenslade'
__license__ = 'GPL / CeCILL'
__copyright__ = 'Copyright 2015 IPSL'


from hermes_client import metrics
from hermes_client import ops
from hermes_client.exceptions import InvalidOptionError
from hermes_client.exceptions import WebServiceException
from hermes_client.utils.logger import log
from hermes_client.options import list_options
from hermes_client.options import OPT_WEB_API_URL
from hermes_client.options import set_option