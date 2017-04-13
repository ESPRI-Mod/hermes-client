# -*- coding: utf-8 -*-

"""
.. module:: decoder_pcmdi_2.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Decodes metrics in 'pcmdi v2' format.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
def _get_models(data):
    """Returns set of models defined within an input file.

    """
    return data['RESULTS'].keys()


def _get_reference_types(data):
    """Returns set of reference types defined within an input file.

    """
    return [(i, u"{}Reference".format(i))  for i in set(data['References'].keys())]


def _get_simulation(data, model):
    """Returns simulation name.

    """
    return data['RESULTS'][model]['SimulationDescription']['Realization']


def _get_regions(data):
    """Returns set of regional maskings defined within an input file.

    """
    return data['RegionalMasking'].keys()


def _get_variable(data):
    """Returns variable name within an input file.

    """
    if 'level' in data['Variable']:
        return "{}-{}".format(data['Variable']['id'], int(data['Variable']['level']))
    return data['Variable']['id']


def _get_metrics(data, reference_type_key, model, simulation, masking):
    """Returns collection of metrics.

    """
    result = dict()

    metrics = data['RESULTS'][model][reference_type_key][simulation][masking]
    for metric_name in metrics:
        for period in metrics[metric_name]:
            result["{}_{}".format(metric_name, period)] = metrics[metric_name][period]

    return result


def _get_groups(data):
    """Returns set of metric groups defined within an input file.

    """
    result = []
    for reference_type, reference_type_key in _get_reference_types(data):
        variable = _get_variable(data)
        for model in _get_models(data):
            simulation = _get_simulation(data, model)
            for region in _get_regions(data):
                masking = region
                try:
                    result.append((
                        reference_type,
                        model,
                        simulation,
                        masking,
                        region,
                        variable,
                        _get_metrics(data, reference_type_key, model, simulation, masking)
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
