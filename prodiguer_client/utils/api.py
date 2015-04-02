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

from prodiguer_client.utils import exceptions



# API base endpoints.
_API = {
    "dev": r"http://localhost:8888",
    "test": r"https://prodiguer-test-web.ipsl.fr",
    "prod": r"https://prodiguer-web.ipsl.fr"
}


def get_endpoint(route, mode='dev'):
    """Returns an API endpoint for invocation.

    """
    return r"{0}{1}".format(_API[mode] , route)


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
        raise exceptions.ProdiguerClientException(response['error'])

    return response
