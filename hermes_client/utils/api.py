# -*- coding: utf-8 -*-

"""
.. module:: api.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: HERMES web-service API utility functions.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import json

import requests

from hermes_client import exceptions
from hermes_client import options



def get_endpoint(route):
    """Returns an API endpoint for invocation.

    """
    base_url = options.get_option(options.OPT_WEB_API_URL)

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
    response = verb(endpoint, data=data, headers=headers, verify=False)
    if response.status_code != 200:
        raise exceptions.WebServiceException(endpoint, {
            'error': response.reason,
            'errorType': response.status_code
            })

    # Decode API response.
    response = response.json()

    # Raise errors.
    if 'error' in response:
        raise exceptions.WebServiceException(endpoint, response)

    return response
