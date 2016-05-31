# -*- coding: utf-8 -*-

"""
.. module:: hermes_client/ops/api_proxy.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Proxy to the remote ops web-service API.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import logging

from prodiguer_client.utils import api
from prodiguer_client.utils import logger



# Reduce requests logging to warnings + errors only.
logging.getLogger("requests").setLevel(logging.WARNING)

# API endpoints.
_EP_HEARTBEAT = r"/api/1/ops/heartbeat"



def _log(action, msg=None):
    """Logger helper function.

    """
    if not msg:
        msg = action
    else:
        msg = "{0} :: {1}".format(action.upper(), msg)
    logger.log(msg, module="OPS")


def heartbeat():
    """Tests to see if remote API is up.

    :raises prodiguer_client.exceptions.WebServiceException: If the web-service reports an error.

    """
    # Invoke API.
    endpoint = api.get_endpoint(_EP_HEARTBEAT)
    api.invoke(endpoint)

    # Inform user.
    _log("heartbeat", \
         "Remote API is up and running")

