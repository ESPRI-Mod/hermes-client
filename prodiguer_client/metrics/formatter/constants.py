# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/metrics/formatter/constants.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Constants used across the package.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
# Supported input formats.
INPUT_FORMAT_1 = "1"
INPUT_FORMAT_2 = "2"

# Set of supported input formats.
INPUT_FORMAT_SET = set([
	INPUT_FORMAT_1,
	INPUT_FORMAT_2
	])

# Supported output formats.
OUTPUT_FORMAT_BLOCKS = 'blocks'

# Set of supported output formats.
OUTPUT_FORMAT_SET = set([
	OUTPUT_FORMAT_BLOCKS,
	])
