#!/bin/sh
# Run the pyessv test suite.
#

PRODIGUER_CLIENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $PRODIGUER_CLIENT_DIR
export PYTHONPATH=PYTHONPATH:$PRODIGUER_CLIENT_DIR
nosetests -v -s tests
