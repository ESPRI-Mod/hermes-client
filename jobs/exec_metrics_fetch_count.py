# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_fetch_count.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches count of metrics within a set of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse


import hermes_client as hermes



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches count of metrics within a set of metrics.")
_parser.add_argument(
    "-g", "--group",
    help="ID of a metrics group",
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
    count = hermes.metrics.fetch_count(args.group, args.filter)
    hermes.log("fetch-count :: {}".format(count), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
