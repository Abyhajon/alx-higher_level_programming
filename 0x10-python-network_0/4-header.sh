#!/bin/bash
# Send a GET request to the URL passed as the first argument, include a custom header variable, and display the body of the response.
curl -s -H 'X-School-User-Id: 98' $1
