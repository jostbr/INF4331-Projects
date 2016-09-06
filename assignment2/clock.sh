
#!/bin/bash

# Initiating an infinite loop (that can be interupted by Ctrl+Z or
# Ctrl+Z) and displaying the time in the requested format by using
# the date command with the %r option for AM/PM-mode and %H%M%S for
# 24h-mode. If user fails to provide valid arg, program terminates.
while [ true ]; do
	clear				# Clears to avoid cluttered terminal.

	case "$1" in
		--AMPM) echo "Displaying time in AM/PM-format:"; date +%r; ;;
		"")		echo "Displaying time in 24h-format:"; date +%H:%M:%S; ;;
		*)		echo "$0: Not a valid format \"$1\""; exit; ;;
	esac

	sleep 1				# Sleeps 1sec to ensure next print is nex sec.
done