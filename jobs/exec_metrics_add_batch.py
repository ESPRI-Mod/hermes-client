# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_add_batch.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Uploads a batch of simulation metrics to the remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Uploads simulation metrics to remote repository.")
_parser.add_argument(
    "-d", "--directory",
    help="Path to a directory in which are metrics files to be uploaded to server",
    dest="directory",
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
    prodiguer.metrics.add_batch(args.directory, args.duplicate_action)


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
