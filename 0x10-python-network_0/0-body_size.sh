#!/usr/bin/env bash
# displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
