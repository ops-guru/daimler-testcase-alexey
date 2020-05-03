#!/bin/bash
#

TARGET="${1:-opsguru-ag-challenge:latest}"
eval $(minikube docker-env)
docker build -t "$TARGET" .
eval $(minikube docker-env -u)