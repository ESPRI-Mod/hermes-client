# -*- coding: utf-8 -*-

"""
.. module:: prodiguer.exceptions.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runtime exceptions thrown by package.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ProdiguerClientException(Exception):
    """Default package exception class.

    """

    def __init__(self, msg):
        """Object constructor.

        """
        self.message = unicode(msg)


    def __str__(self):
        """Returns a string representation.

        """
        return "IPSL PRODIGUER EXCEPTION : {0}".format(repr(self.message))

