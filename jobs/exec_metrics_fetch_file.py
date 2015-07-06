# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_file.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches a set of metrics and saves them to local file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse
import os
import shutil

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches a set of metrics and saves them to local file system.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )
_parser.add_argument(
    "-f", "--filter",
    help="Path to a metrics filter to be applied",
    dest="filter",
    type=str,
    default=None
    )
_parser.add_argument(
    "-o", "--output-dir",
    help="Directory to which downloaded metrics files will be written",
    dest="output_dir",
    type=str
    )



def _main(args):
    """Main entry point.

    """
    input_file = prodiguer.metrics.fetch_file(args.group, args.filter)
    output_file = "{}.json".format(os.path.join(args.output_dir, args.group))
    shutil.move(input_file, output_file)
    prodiguer.log("fetch-file :: {}".format(output_file, module="METRICS"))



# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
