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

# Check for "<html" in the body
if [[ "$response" == *"<html"* ]]; then
    echo "'<html' test passed"
else
    echo "'<html' test failed"
fi

# Check for "Getting Started with Docker" in the body
if [[ "$response" == *"Getting Started with Docker"* ]]; then
    echo "'Getting Started with Docker' test passed"
else
    echo "'Getting Started with Docker' test failed"
fi

# Check for "</html>" in the body
if [[ "$response" == *"</html>"* ]]; then
    echo "'</html>' test passed"
else
    echo "'</html>' test failed"
fi