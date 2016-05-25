#!/bin/sh
# Run the pyessv test suite.
#

HERMES_CLIENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $HERMES_CLIENT_DIR
export PYTHONPATH=PYTHONPATH:$HERMES_CLIENT_DIR
nosetests -v -s tests
