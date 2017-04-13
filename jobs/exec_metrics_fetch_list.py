# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_fetch_list.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches list of all metric groups.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import hermes_client as hermes



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches list of all metric groups.")


def _main():
    """Main entry point.

    """
    groups = hermes.metrics.fetch_list()
    for group in groups:
        hermes.log("list :: {}".format(group), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _parser.parse_args()
    _main()
