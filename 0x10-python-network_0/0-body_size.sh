#!/bin/bash
#A bash script that takes in a URL, sends request
#to uRl and
# displays the size of the body of the response
curl -s "$1" | wc -c
