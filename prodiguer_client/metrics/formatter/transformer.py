# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client/metrics/formatter/transformer.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Transformer metrics from one format to standardized format.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from prodiguer_client.metrics.formatter import transformer_pcmdi



# Map of supported transformers keyed by file format.
_TRANSFORMERS = {
    'pcmdi': transformer_pcmdi.transform
}


def transform(input_data, input_format):
    """Transforms input data to standardized format.

    :param list input_data: Metrics json file data.
    :param str input_format: Format of metrics files.

    :returns: Input data transformed to standardized format.
    :rtype: list

    """
    transformer = _TRANSFORMERS[input_format]
    data, groups = input_data

    return [transformer(data, group) for group in groups]
