# -*- coding: utf-8 -*-

"""
.. module:: prodiguer/ops/jobs/api/metric/run_fetch_file.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches a set of metrics and saves them to local file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os
import shutil

from tornado.options import define
from tornado.options import options
import prodiguer_client as prodiguer



# Define command line options.
define("group",
       help="ID of a metrics group")
define("filter",
       default=None,
       help="Path to a metrics filter to be applied")
define("output_dir",
       type=str,
       help="Path to which downloaded metrics files will be written.")



def _main():
    """Main entry point.

    """
    input_file = prodiguer.metrics.fetch_file(options.group, options.filter)
    output_file = "{}.json".format(os.path.join(options.output_dir, options.group))
    shutil.move(input_file, output_file)
    prodiguer.log("fetch-file :: {}".format(output_file, module="METRICS"))



# Main entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
