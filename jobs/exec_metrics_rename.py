# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_rename.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Renames a group of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options
import prodiguer_client as prodiguer



# Define command line options.
define("group",
       type=str,
       help="Name of metrics group to be renamed (e.g. cmip5-1).")
define("new_name",
       type=str,
       help="New group name.")
define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    prodiguer.metrics.rename(options.group, options.new_name)


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
