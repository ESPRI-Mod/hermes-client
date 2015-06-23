# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_rename.py
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
    help="ID of a metrics group to be renamed",
    dest="group",
    type=str
    )
_parser.add_argument(
    "-n", "--new-name",
    help="New group name.",
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
