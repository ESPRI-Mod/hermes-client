# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_format.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Formats simulation metrics in readiness for upload.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Formats simulation metrics in readiness for upload.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )
_parser.add_argument(
    "-i", "--input-dir",
    help="Directory containing unformatted metrics files",
    dest="input_dir",
    type=str
    )
_parser.add_argument(
    "-o", "--output-dir",
    help="Directory to which reformatted metrics files will be written",
    dest="output_dir",
    type=str
    )


def _main(args):
    """Main entry point.

    """
    prodiguer.metrics.format(args.group,
                             args.input_dir,
                             args.output_dir)


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
