#!/bin/bash
# script sends a Post to the passed url and returns the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
