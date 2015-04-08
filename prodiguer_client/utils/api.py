# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client/utils/api.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: API utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import json, requests

from prodiguer_client import exceptions, options



def get_endpoint(route):
    """Returns an API endpoint for invocation.

    """
    base_url = options.get_option(options.OPT_API_URL)

    return r"{0}{1}".format(base_url, route)


def invoke(endpoint, verb=requests.get, payload=None):
    """Invokes api endpoint.

    """
    # Prepare request info.
    data = headers = None
    if payload:
        headers = {'content-type': 'application/json'}
        data = json.dumps(payload)

    # Invoke API.
    response = verb(endpoint, data=data, headers=headers).json()

    # Raise errors.
    if 'error' in response:
        raise exceptions.WebServiceException(endpoint, response)

    return response
