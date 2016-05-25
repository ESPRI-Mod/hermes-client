# Set path to ./jobs.
declare HERMES_CLIENT_DIR_JOBS="$( dirname "${BASH_SOURCE[0]}" )"/jobs

# Supported commands.
declare -a HERMES_CLIENT_COMMANDS=(
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
for HERMES_CLIENT_COMMAND in "${HERMES_CLIENT_COMMANDS[@]}"
do
	declare HERMES_CLIENT_JOB=`echo $HERMES_CLIENT_COMMAND | tr '[:upper:]' '[:lower:]' | tr '-' '_'`
	alias hermes-client-$HERMES_CLIENT_COMMAND='python '$HERMES_CLIENT_DIR_JOBS'/exec_'$HERMES_CLIENT_JOB'.py'
done

# Unset work vars.
unset HERMES_CLIENT_DIR_JOBS
unset HERMES_CLIENT_COMMAND
unset HERMES_CLIENT_COMMANDS
unset HERMES_CLIENT_JOB
