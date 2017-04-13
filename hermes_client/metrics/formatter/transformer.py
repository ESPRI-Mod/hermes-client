# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/metrics/formatter/transformer.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Transformer metrics from one format to standardized format.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
from hermes_client.metrics.formatter import constants
from hermes_client.metrics.formatter import transformer_pcmdi_1
from hermes_client.metrics.formatter import transformer_pcmdi_2



# Map of transformers to input formats.
_TRANSFORMERS = {
    constants.INPUT_FORMAT_1: transformer_pcmdi_1,
    constants.INPUT_FORMAT_2: transformer_pcmdi_2
}


def transform(input_data, input_format):
    """Transforms input data to standardized format.

    :param list input_data: Metrics json file data.

    :returns: Input data transformed to standardized format.
    :rtype: list

    """
    data, groups = input_data
    transformer = _TRANSFORMERS[input_format]

    return [transformer.transform(data, group) for group in groups]
