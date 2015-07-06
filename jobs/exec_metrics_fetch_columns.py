# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_columns.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches columns associated with a set of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import prodiguer_client as prodiguer



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches columns associated with a set of metrics.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )



def _main(args):
    """Main entry point.

    """
    columns = prodiguer.metrics.fetch_columns(args.group)
    for column in sorted(columns):
        prodiguer.log("fetch-columns :: {}".format(column), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
