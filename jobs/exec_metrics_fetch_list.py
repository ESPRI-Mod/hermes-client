# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_list.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches list of all metric groups.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options

import prodiguer_client as prodiguer



define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    groups = prodiguer.metrics.fetch_list()
    for group in groups:
        prodiguer.log("list :: {}".format(group), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
