# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches simulation metrics from remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches simulation metrics from remote repository.")
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
    data = prodiguer.metrics.fetch(args.group, args.filter)
    prodiguer.log("fetch :: {}".format(data), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
