# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_columns.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches columns associated with a set of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options
import prodiguer_client as prodiguer



# Define command line options.
define("group",
       help="ID of a metrics group")
define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    columns = prodiguer.metrics.fetch_columns(options.group)
    for column in sorted(columns):
        prodiguer.log("fetch-columns :: {}".format(column), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
