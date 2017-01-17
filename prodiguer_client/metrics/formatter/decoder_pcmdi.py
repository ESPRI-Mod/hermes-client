# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/metrics/formatter/decoder_pcmdi.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Decodes metrics in 'pcmdi' format.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import os



def _get_models(data):
    """Returns set of models defined within an input file.

    """
    result = set()
    for key, val in data.iteritems():
        try:
            val['SimulationDescription']
        except (TypeError, KeyError):
            pass
        else:
            result.add(key)

    return result


def _get_reference_types(data):
    """Returns set of reference types defined within an input file.

    """
    return [(i, u"{}Reference".format(i))  for i in set(data['References'].keys())]


def _get_simulations(data):
    """Returns set of simulations defined within an input file.

    """
    result = set()
    for model in _get_models(data):
        for name in ['Realization', 'SimName']:
            if name in data[model]['SimulationDescription']:
                result.add(data[model]['SimulationDescription'][name])
                break

    return result


def _get_maskings(data):
    """Returns set of regional maskings defined within an input file.

    """
    result = set()
    for model in _get_models(data):
        for reference_type, reference_type_key in _get_reference_types(data):
            for simulation in _get_simulations(data):
                result.update(data[model][reference_type_key][simulation].keys())

    return result


def _get_groups(data):
    """Returns set of metric groups defined within an input file.

    """
    result = []
    for reference_type, reference_type_key in _get_reference_types(data):
        variable = data['References'][reference_type]['filename'].split("_")[0]
        for model in _get_models(data):
            for simulation in _get_simulations(data):
                for masking in _get_maskings(data):
                    try:
                        result.append((
                            reference_type,
                            model,
                            simulation,
                            masking,
                            variable,
                            data[model][reference_type_key][simulation][masking]
                            ))
                    except KeyError:
                        pass

    return result


def decode(data):
    """Decodes set of metrics files.

    :param list data: Raw metrics data.

    :returns: Input data to be transformed.
    :rtype: list

    """
    return (data, _get_groups(data))
