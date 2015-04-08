# Root alias.
DIR_PRODIGUER_CLIENT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PRODIGUER_CLIENT='$DIR_PRODIGUER_CLIENT/shell/exec.sh'

# Supported command types.
declare -a command_types=(
	metrics
)

# Supported commands.
declare -a commands=(
	metrics-add
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
)

# Create command aliases.
for command in "${commands[@]}"
do
	alias prodiguer-client-$command=$PRODIGUER_CLIENT" "$command
done

# Create command type help aliases.
for command_type in "${command_types[@]}"
do
	alias help-prodiguer-client-$command_type=$PRODIGUER_CLIENT" help-"$command_type
done

# Create command help aliases.
for command in "${commands[@]}"
do
	alias help-prodiguer-client-$command=$PRODIGUER_CLIENT" help-"$command
done
