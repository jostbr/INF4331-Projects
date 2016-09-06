
#!/bin/bash

# All arguments are assumed to be of type "integer".

# All variables to hold their respective result are initialized
# to the first integer-argument. $1 is the operation specifier.
declare -i sum=$2
declare -i product=$2
declare -i maximum=$2
declare -i minimum=$2

# Here we go through (starting from the second integer-argument) all
# arguments and execute appropriate operations, depending on user
# specified operation, to get wanted results. Then prints to screen.
# Comment: All loops are separately implemented in each of the case
# statements so that only the requested quanity is computed and not
# all the other three as well.
case "$1" in
	S) 
		for num in ${@:3}; do
			sum=${sum}+${num}
		done; echo "$sum";	;;
	P)
		for num in ${@:3}; do
			product=${product}*${num}
		done; echo "$product"; ;;
	M)
		for num in ${@:3}; do
			[ $num -gt $maximum ] && maximum=$num
		done; echo "$maximum"; ;;
	m)
		for num in ${@:3}; do
			[ $num -lt $minimum ] && minimum=$num
		done; echo "$minimum"; ;;
	*)
		echo "$0: Invalid operation \"$1\""; exit ;;
esac
