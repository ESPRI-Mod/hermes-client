# Extend python path.
declare _DIR="$( dirname "${BASH_SOURCE[0]}" )"
export PYTHONPATH=$PYTHONPATH:$_DIR

# Set path to ./jobs.
declare _DIR_JOBS="$( dirname "${BASH_SOURCE[0]}" )"/jobs

# Supported commands.
declare -a _commands=(
	metrics-add
	metrics-add-batch
	metrics-delete
	metrics-fetch
	metrics-fetch-columns
	metrics-fetch-count
	metrics-fetch-file
	metrics-fetch-setup
	metrics-fetch-list
	metrics-format
	metrics-rename
	metrics-set-hashes
	ops-heartbeat
)

# Create command aliases.
for _command in "${_commands[@]}"
do
	declare _job=`echo $_command | tr '[:upper:]' '[:lower:]' | tr '-' '_'`
	alias prodiguer-client-$_command='python '$_DIR_JOBS'/exec_'$_job'.py'
done

# Unset work vars.
unset _DIR_JOBS
unset _command
unset _commands
unset _job
