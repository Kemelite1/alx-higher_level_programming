#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument
# and displays only the status code of the response.

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send the HTTP request and extract the status code using curl
status_code=$(curl -sI "$1" | awk 'NR==1{print $2}')

# Display the status code
echo "Status Code: $status_code"
