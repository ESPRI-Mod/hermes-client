# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_set_hashes.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Reassigns hash identifiers for a group of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Reassigns hash identifiers for a group of metrics.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )


def _main(args):
    """Main entry point.

    """
    prodiguer.metrics.set_hashes(args.group)


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
