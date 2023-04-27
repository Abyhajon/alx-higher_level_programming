#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl -I -X OPTIONS -s $1 | grep "Allow" | cut -d' ' -f2-
