# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_add_batch.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Uploads simulation metrics to remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options
import prodiguer_client as prodiguer



# Define command line options.
define("directory",
       help="Path to a directory in which are metrics files to be uploaded to server")
define("duplicate_action",
       help="Action to take when adding a metric with a duplicate hash identifier")
define("api_url",
       default=r"http://localhost:8888",
       help="API base URL.")


def _main():
    """Main entry point.

    """
    prodiguer.set_option(prodiguer.OPT_API_URL, options.api_url)

    prodiguer.metrics.add_batch(options.directory, options.duplicate_action)


# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
