#!/bin/bash
#A bash script that takes in a URL, sends request
#and displays size ofthe body response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
