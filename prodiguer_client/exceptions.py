# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client.exceptions
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runtime exceptions thrown by package.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import arrow



class ProdiguerClientException(Exception):
    """Default package exception class.

    """
    def __init__(self, msg):
        """Instance constructor.

        """
        self.message = unicode(msg)
        self.timestamp = unicode(arrow.get())

    def __str__(self):
        """Instance string representation.

        """
        return "IPSL HERMES CLIENT EXCEPTION : {0}".format(repr(self.message))


class InvalidOptionError(ProdiguerClientException):
    """An error raised when user tries to access an invalid option.

    """
    def __init__(self, option):
        """Instance constructor.

        """
        msg = "Unsupported option: {}".format(option)
        super(InvalidOptionError, self).__init__(msg)


class WebServiceException(ProdiguerClientException):
    """Web service exception class.

    """
    def __init__(self, endpoint, response):
        """Instance constructor.

        """
        super(WebServiceException, self).__init__(response['error'])

        self.endpoint = endpoint
        self.error_type = response['errorType']

    def __str__(self):
        """Instance string representation.

        """
        text = """
        IPSL HERMES WEB SERVICE API EXCEPTION :
        \tTimestamp = {0}
        \tEndpoint = {1}
        \tError = {2}
        \tError Type = {3}
        """

        return text.format(
            self.timestamp,
            self.endpoint,
            self.message,
            self.error_type
            )
