# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_delete.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Deletes simulation metrics from remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options
import prodiguer_client as prodiguer



# Define command line options.
define("group",
       help="ID of a metrics group")
define("filter",
       default=None,
       help="Path to a metrics filter to be applied prior to deletion")
define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    prodiguer.metrics.delete(options.group, options.filter)



# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
