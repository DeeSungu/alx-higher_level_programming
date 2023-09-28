#!/bin/bash
# Displays the body of the response of a curl request.
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
