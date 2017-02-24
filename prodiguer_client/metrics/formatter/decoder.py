# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/metrics/formatter/decoder.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Decodes metrics.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import json

from prodiguer_client.metrics.formatter import constants
from prodiguer_client.metrics.formatter import decoder_pcmdi_1
from prodiguer_client.metrics.formatter import decoder_pcmdi_2



# Map of decoaders to input formats.
_DECODERS = {
    constants.INPUT_FORMAT_1: decoder_pcmdi_1,
    constants.INPUT_FORMAT_2: decoder_pcmdi_2
}


def decode(input_file):
    """Decodes set of metrics files.

    :param str input_file: An input file to be decoded.
    :param str input_format: Metrics format of input file.

    :returns: Input data to be processed.
    :rtype: list

    """
    # Load JSON data.
    with open(input_file, 'r') as fstream:
        input_data = json.loads(fstream.read())

    # Determine input format.
    input_format = constants.INPUT_FORMAT_2 if "json_version" in input_data else constants.INPUT_FORMAT_1

    return _DECODERS[input_format].decode(input_data), input_format
