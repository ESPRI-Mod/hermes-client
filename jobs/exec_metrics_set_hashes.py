# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_set_hashes.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Reassigns hash identifiers for a group of metrics.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options
import prodiguer_client as prodiguer



# Define command line options.
define("group",
       type=str,
       help="Name of metrics group whose hash identifiers are to be reset (e.g. cmip5-1).")
define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    prodiguer.metrics.set_hashes(options.group)


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
