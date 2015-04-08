#!/bin/bash

# ###############################################################
# SECTION: INITIALIZATION
# ###############################################################

declare -a initializers=(
	'init_action'
	'init_helpers'
	'init_paths'
	'exec_metrics'
	'help'
	'help_metrics'
)
for initializer in "${initializers[@]}"
do
	source $DIR/$initializer.sh
done
