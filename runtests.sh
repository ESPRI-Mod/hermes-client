#!/bin/sh
# Run the pyessv test suite.
#

HERMES_CLIENT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $HERMES_CLIENT_HOME
export PYTHONPATH=PYTHONPATH:$HERMES_CLIENT_HOME
nosetests -v -s tests
