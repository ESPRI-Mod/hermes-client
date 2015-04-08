# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_list.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches list of all metric groups.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import prodiguer_client as prodiguer



def _main():
    """Main entry point.

    """
    groups = prodiguer.metrics.fetch_list()
    for group in groups:
        prodiguer.log("list :: {}".format(group), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
