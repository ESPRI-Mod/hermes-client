# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_rename.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Renames a group of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Renames a group of metrics.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )
_parser.add_argument(
    "-n", "--new-name",
    help="New metrics group identifier",
    dest="new_name",
    type=str
    )


def _main(args):
    """Main entry point.

    """
    prodiguer.metrics.rename(args.group, args.new_name)


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
