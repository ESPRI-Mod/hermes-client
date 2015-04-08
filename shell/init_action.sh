#!/bin/bash

# ###############################################################
# SECTION: INITIALIZE ACTION
# ###############################################################

# Set action.
declare ACTION=`echo $1 | tr '[:upper:]' '[:lower:]' | tr '-' '_'`
if [[ $ACTION == help_* ]]; then
	:
elif [[ $ACTION != exec_* ]]; then
	declare ACTION="exec_"$ACTION
fi

# Set action argument.
declare ACTION_ARG=$2

# Set action sub-arguments.
declare ACTION_SUBARG1=$3
declare ACTION_SUBARG2=$4
declare ACTION_SUBARG3=$5
declare ACTION_SUBARG4=$6
