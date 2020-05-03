#!/bin/bash
#

RELEASE="${1:-opsguru-ag-challenge}"
IMAGE="${2:-opsguru-ag-challenge}"

helm install -n "$RELEASE" --set "image.repository=$IMAGE" ./helm