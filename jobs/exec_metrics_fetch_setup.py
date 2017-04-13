# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_fetch_setup.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches setup data associated with a set of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import hermes_client as hermes



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches setup data associated with a set of metrics.")
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


def _main(args):
    """Main entry point.

    """
    data = hermes.metrics.fetch_setup(args.group, args.filter)
    for key in data.keys():
        hermes.log("{0} :: {1}".format(key, data[key]), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
