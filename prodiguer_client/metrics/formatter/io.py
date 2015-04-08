# -*- coding: utf-8 -*-

"""
.. module:: prodiguer_client/metrics/formatter/io.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Decodes metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob, os, json

from prodiguer_client.metrics.formatter import constants



def init_output_dir(output_dir):
    """Initializes output directory into which metrics will be written.

    """
    def _init(target_dir):
        """Initializes a target dir.

        """
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        else:
            for fpath in glob.glob(os.path.join(target_dir, "*.json")):
                os.remove(fpath)

    for output_format in constants.OUTPUT_FORMAT_SET:
        _init(os.path.join(output_dir, output_format))


def write(data, output_dir, output_format, output_file_name):
    """Writes formatted metrics data to file system.

    :param dict data: Data (dictionary format) to be written to file system.
    :param str output_dir: Path to output directory.
    :param str output_file: Name of output file.

    """
    fpath = os.path.join(output_dir, output_format)
    fname = "{}.json".format(output_file_name)
    fpath = os.path.join(fpath, fname)
    with open(fpath, 'w') as f:
        f.write(json.dumps(data, indent=4))


def get_input_files(input_dir):
    """Returns set of input files for processing.

    """
    result = glob.glob(os.path.join(input_dir, "*.json"))
    for sub_dir in next(os.walk(input_dir))[1]:
        result += get_input_files(os.path.join(input_dir, sub_dir))

    return result
