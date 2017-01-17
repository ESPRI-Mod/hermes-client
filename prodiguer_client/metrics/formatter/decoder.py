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

from prodiguer_client.metrics.formatter import decoder_pcmdi
from prodiguer_client.metrics.formatter import constants



# Map of supported decoders keyed by file format.
_DECODERS = {
    constants.INPUT_FORMAT_PCMDI: decoder_pcmdi.decode
}


def decode(input_file, input_format):
    """Decodes set of metrics files.

    :param str input_file: An input file to be decoded.
    :param str input_format: Metrics format of input file.

    :returns: Input data to be processed.
    :rtype: list

    """
    decoder = _DECODERS[input_format]
    with open(input_file, 'r') as fstream:
        input_data = json.loads(fstream.read())

    return decoder(input_data)
