
#!/bin/bash

# This code is based on the layout of the HTML-file from Ruter as, it was while creating this code, meaning 06.09.16.
# If Ruter has changed the layout/form of their HTML-code since then, the code might not work properly. The info about
# number of colons ":", used below, was gathered by counting through looking at the HTML-file.

# Default variables.
HTML_FILE=$(curl -s https://ruter.no/reiseplanlegger/Stoppested/%283010370%29Forskningsparken%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0)
station="Forskningsparken"
direction="NONE"

# Handles invalid number of arguments.
if [ $# -gt 2 ]; then
	echo "Error: Too many arguments. Provide 2 or 0"
	exit
elif [[ $# -eq 1 && "$1" != "Forskningsparken" && "$1" != "Blindern" && "$1" != "Nydalen" ]]; then
	echo "Invalid argument; provide nothing, one station, or one station and one direction"
	exit
fi

# Setting URL to station corresponding to user input.
for arg in $@; do
	if [ $arg == "Forskningsparken" ]; then
		station=$arg
		HTML_FILE=$(curl -s https://ruter.no/reiseplanlegger/Stoppested/%283010370%29Forskningsparken%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0)

	elif [ $arg == "Blindern" ]; then
		station=$arg
		HTML_FILE=$(curl -s https://ruter.no/reiseplanlegger/Stoppested/%283010360%29Blindern%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0)

	elif [ $arg == "Nydalen" ]; then
		station=$arg
		HTML_FILE=$(curl -s https://ruter.no/reiseplanlegger/Stoppested/%283012130%29Nydalen%20%5BT-bane%5D%20%28Oslo%29/Avganger/#st:1,sp:0,bp:0)

	elif [ $arg == "--E" ]; then
		direction=$arg

	elif [ $arg == "--W" ]; then
		direction=$arg
	fi
done

# Extracts the relevant line by using grep on a word that
# is only in the wanted line. In this case: "BoardingAllowed".
departures_line=$(echo "$HTML_FILE" | grep -m 1 "BoardingAllowed")

# Function that extracts the departure subway given the number ($1) of colons ":" before the station name.
function get_departure_subway {
	echo "$departures_line" | cut -d":" -f $1 | cut -d"\"" -f 2
}

# Function that extracts the departure time for a subway given the number ($1 (part 1), $2 (part 2)) of colons ":" before the station name.
function get_departure_time {
	departure_time_pt1=$(echo "$departures_line" | cut -d":" -f $1 | cut -d"\"" -f 2)
	departure_time_pt2=$(echo "$departures_line" | cut -d":" -f $2 | cut -d"\"" -f 1)
	departure_time=$departure_time_pt1":"$departure_time_pt2
	echo "$departure_time"
}

# ----------------- WEST -------------------
first_subway_west=$(get_departure_subway 46)
first_time_west=$(get_departure_time 55 56)

second_subway_west=$(get_departure_subway 94)
second_time_west=$(get_departure_time 103 104)

third_subway_west=$(get_departure_subway 142)
third_time_west=$(get_departure_time 151 152)

# ----------------- EAST -------------------
first_subway_east=$(get_departure_subway 193)
first_time_east=$(get_departure_time 202 203)

second_subway_east=$(get_departure_subway 241)
second_time_east=$(get_departure_time 250 251)

third_subway_east=$(get_departure_subway 289)
third_time_east=$(get_departure_time 298 299)

# Printing desired results when applying the flag --W. Then more
# if's inside take care of the cases for each of the stations.
if [[ "$direction" == "--W" ]]; then
	if [[ "$station" == "Forskningsparken" || "$station" == "Blindern" ]]; then
		echo "Subways going westbound at $station:";
		echo -n "$first_time_west - "; echo "$first_subway_west"; echo -n "$second_time_west - ";
		echo "$second_subway_west"; echo -n "$third_time_west - "; echo "$third_subway_west\n";

	elif [[ "$station" == "Nydalen" ]]; then
		echo "Subways going westbound at $station:";
		echo -n "$first_time_west - "; echo "$first_subway_west";
		echo -n "$second_time_west - "; echo "$second_subway_west";
	fi

# Printing desired results when applying the flag --E. Then more
# if's inside take care of the cases for each of the stations.
elif [[ "$direction" == "--E" ]]; then
	if [[ "$station" == "Forskningsparken" || "$station" == "Blindern" ]]; then
		echo "Subways going eastbound at $station:";
		echo -n "$first_time_east - "; echo "$first_subway_east"; echo -n "$second_time_east - ";
		echo "$second_subway_east"; echo -n "$third_time_east - "; echo "$third_subway_east";

	elif [[ "$station" == "Nydalen" ]]; then
		echo "Subways going eastbound at $station";
		echo -n "$first_time_east - "; echo "$first_subway_east";
		echo -n "$second_time_east - "; echo "$second_subway_east";
	fi

# Printing desired results when not usin flag or no argument at all.
# Then more if's inside take care of the cases for each of the stations.
elif [[ $# -eq 0 || $# -eq 1 ]]; then
	if [[ "$station" == "Forskningsparken" || "$station" == "Blindern" ]]; then
		echo "Subways going westbound at $station:";
		echo -n "$first_time_west - "; echo "$first_subway_west"; echo -n "$second_time_west - ";
		echo "$second_subway_west"; echo -n "$third_time_west - "; echo "$third_subway_west";
		echo ""; echo "Subways going eastbound at $station";
		echo -n "$first_time_east - "; echo "$first_subway_east"; echo -n "$second_time_east - ";
		echo "$second_subway_east"; echo -n "$third_time_east - "; echo "$third_subway_east";
	elif [[ "$station" == "Nydalen" ]]; then
		echo "Subways going westbound at $station:";
		echo -n "$first_time_west - "; echo "$first_subway_west";
		echo -n "$second_time_west - "; echo "$second_subway_west";
		echo ""; echo "Subways going eastbound at $station";
		echo -n "$first_time_west - "; echo "$first_subway_west";
		echo -n "$second_time_west - "; echo "$second_subway_west";
	fi
fi
