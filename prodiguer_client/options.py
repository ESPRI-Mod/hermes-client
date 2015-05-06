# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client.options
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Manages user assignable library options.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import os

from prodiguer_client import exceptions
from prodiguer_client.utils import logger



# OPTION: URL to web api.
OPT_WEB_API_URL = "web-api-url"

# OPTION: logging is verbose.
OPT_IS_VERBOSE = "verbose"

# Name of web api url environment variable.
_WEB_API_URL_ENV_VAR = 'PRODIGUER_CLIENT_WEB_URL'

# Default web api url environment variable.
_WEB_API_URL_DEFAULT = r"https://prodiguer-test-web.ipsl.fr"

# Map of supported options and their default values.
_OPTIONS = {
    OPT_WEB_API_URL : os.getenv(_WEB_API_URL_ENV_VAR, _WEB_API_URL_DEFAULT),
    OPT_IS_VERBOSE: True
}


def _validate_option_name(name):
    """Validates that an option is supported.

    """
    if name not in _OPTIONS:
        raise exceptions.InvalidOptionError(name)


def list_options():
    """Returns tuple of supported library options.

    """
    for name, value in _OPTIONS.items():
        print("OPTION {0} = {1}".format(name, value))


def set_option(name, value):
    """Sets an option value.

    :param str name: Option name.
    :param str value: Option value.

    """
    _validate_option_name(name)
    _OPTIONS[name] = unicode(value)
    logger.log("OPTION: {0} = {1}.".format(name, value))


def get_option(name):
    """Returns an option value.

    :param str name: Option name.

    :returns: A library option.
    :rtype: str

    """
    _validate_option_name(name)

    return _OPTIONS[name]
