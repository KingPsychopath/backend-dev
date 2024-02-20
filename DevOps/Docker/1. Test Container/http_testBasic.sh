#!/bin/bash

# Make a GET request
response=$(curl -s http://localhost:80)

# Check the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:80)
if [ "$status_code" -eq 200 ]; then
    echo "Status code test passed: $status_code"
else
    echo "Status code test failed: $status_code"
fi

# Check the body
if [[ "$response" == *"<html"* && "$response" == *"Getting Started with Docker"* && "$response" == *"</html>"* ]]; then
    echo "Body content test passed: $status_code"
else
    echo "Body content test failed: $status_code"
fi