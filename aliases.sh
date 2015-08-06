# Set path to ./jobs.
declare PRODIGUER_CLIENT_DIR_JOBS="$( dirname "${BASH_SOURCE[0]}" )"/jobs

# Supported commands.
declare -a PRODIGUER_CLIENT_COMMANDS=(
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
for PRODIGUER_CLIENT_COMMAND in "${PRODIGUER_CLIENT_COMMANDS[@]}"
do
	declare PRODIGUER_CLIENT_JOB=`echo $PRODIGUER_CLIENT_COMMAND | tr '[:upper:]' '[:lower:]' | tr '-' '_'`
	alias prodiguer-client-$PRODIGUER_CLIENT_COMMAND='python '$PRODIGUER_CLIENT_DIR_JOBS'/exec_'$PRODIGUER_CLIENT_JOB'.py'
done

# Unset work vars.
unset PRODIGUER_CLIENT_DIR_JOBS
unset PRODIGUER_CLIENT_COMMAND
unset PRODIGUER_CLIENT_COMMANDS
unset PRODIGUER_CLIENT_JOB
