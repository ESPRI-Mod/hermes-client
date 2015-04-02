# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client/utils/api.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: IO utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from prodiguer_client.utils import convert



def parse_filepath(filepath):
    """Parses a filepath.

    """
    if not os.path.exists(filepath) or not os.path.isfile(filepath):
        raise IOError("Invalid file path: {}.".format(filepath))

    return filepath


def parse_dirpath(dirpath):
    """Parses a directory path.

    """
    if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
        raise IOError("Invalid directory path: {}.".format(dirpath))

    return dirpath


def parse_json_filepath(filepath, force=False):
    """Parses a json filepath.

    """
    if filepath or force:
        return convert.json_file_to_dict(parse_filepath(filepath))
