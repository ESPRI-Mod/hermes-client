# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Prodiguer client root package intializer.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
from prodiguer_client.metrics.api_proxy import (
	add,
	add_batch,
	delete,
	fetch,
	fetch_columns,
	fetch_count,
	fetch_file,
	fetch_list,
	fetch_setup,
	rename,
	set_hashes
	)
from prodiguer_client.metrics.formatter.main import execute as format
