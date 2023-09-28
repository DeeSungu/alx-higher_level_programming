#!/bin/bash
#A bash script that takes in a URL, sends request
#and displays size ofthe body response.
curl -so /dev/null -w '%{size_download}\n' "$1"
