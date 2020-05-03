#!/bin/bash
#

TARGET="${1:-opsguru-ag-challenge:latest}"
docker build -t "$TARGET" .