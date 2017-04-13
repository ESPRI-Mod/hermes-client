# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_add.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Uploads simulation metrics to the remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import hermes_client as hermes



# Define command line arguments.
_parser = argparse.ArgumentParser("Uploads simulation metrics to remote repository.")
_parser.add_argument(
    "-f", "--file",
    help="Path to a metrics file to be uploaded to server",
    dest="file",
    type=str
    )
_parser.add_argument(
    "--duplicate-action",
    help="Action to take when adding a metric with a duplicate hash identifier",
    dest="duplicate_action",
    type=str,
    default="skip"
    )



def _main(args):
    """Main entry point.

    """
    hermes.metrics.add(args.file, args.duplicate_action)


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
