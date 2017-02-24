# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/metrics/formatter/transformer_pcmdi.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Transforms metrics in pcdmi format to the standard format.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
from prodiguer_client.metrics.formatter import transformer_utils as tu



def _get_simulation(data, simulation, model):
    """Returns simulation information for output.

    """
    # Set data pointer.
    sim = data['RESULTS'][model]['SimulationDescription']

    result = tu.get_dict({
        'activity': sim['ModelActivity'],
        'checkSum': sim.get('simulationCheckSum', None),
        'computeNode': sim.get('Center', None),
        'creationDate': tu.get_date(sim['creation_date']),
        'experiment': sim['Experiment'],
        'freeSpace': sim.get('ModelFreeSpace', None),
        'inputClimatologyFileName': data['RESULTS'][model].get('InputClimatologyFileName'),
        'inputClimatologyFileCheckSum': data['RESULTS'][model].get('InputClimatologyMD5'),
        'institute': sim.get('ModellingGroup', None),
        'login': sim.get('Login', None),
        'mipTable': sim.get('MIPTable', None),
        'model': model,
        'name': simulation,
        'period': sim.get('Model_period', None),
        'trackingId': sim.get('tracking_id', None)
    })

    if result['login'] == "login_not_defined":
        result['login'] = None
    if result['institute'] == "institute_id_not_defined":
        result['institute'] = None

    return result


def _get_masking(data, regional_masking, region):
    """Returns regional masking information for output.

    """
    return tu.get_dict({
        'region': regional_masking if regional_masking != "global" else "GLB",
        'value': None
    })


def _get_reference(data, reference_type):
    """Returns reference information for output.

    """
    # Set data pointer.
    reference = data['References'][reference_type]

    return tu.get_dict({
        'fileCheckSum': reference['MD5sum'],
        'filename': reference['filename'],
        'name': reference['RefName'],
        'period': reference['period'],
        'trackingDate': tu.get_date(reference['RefTrackingDate']),
        'type': reference_type
    })


def _get_regridding(data):
    """Returns regridding information for output.

    """
    # Set data pointer.
    grid = data['GridInfo']

    return tu.get_dict({
        'method': grid['RegridMethod'],
        'gridName': grid['GridName'],
        'tool': grid['RegridTool'],
    })


def _get_metric(metric):
    """Returns metric information for output.

    """
    name, value = metric

    return {
        'name': name,
        'value': tu.get_numeric(value)
    }


def transform(data, group):
    """Converts a group of metrics for output.

    :param dict data: Metrics json file data.
    :param dict group: Metrics group.

    :returns: Group transformed to a standardized format.
    :rtype: dict

    """
    # Unpack tuple.
    reference_type, model, simulation, masking, region, variable, metrics = group

    # Set simulation data.
    sim = data['RESULTS'][model]['SimulationDescription']

    # Return a dictionary that will be flattened during encoding.
    return tu.get_dict({
        'masking': _get_masking(data, masking, region),
        'metricCreationDate': sim.get('metricCreationDate', None),
        'metrics': [_get_metric(m) for m in metrics.iteritems()],
        'reference': _get_reference(data, reference_type),
        'regridding': _get_regridding(data),
        'simulation': _get_simulation(data, simulation, model),
        'variable': variable
    })
