#!/bin/bash
# Returns methods a server supports
curl -si -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
