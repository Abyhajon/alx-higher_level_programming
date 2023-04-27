#!/usr/bin/env bash
# cURL request that displays size of the response's body.
curl -s -w '%{size_download}\n' -o /dev/null "$1" | tail -n 1
