# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Prodiguer client root package intializer.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
from prodiguer_client import metrics
from prodiguer_client import ops
from prodiguer_client.utils.runtime import log
from prodiguer_client.options import (
	OPT_WEB_API_URL,
	set_option
	)


__version__ = '0.1.0.0'
