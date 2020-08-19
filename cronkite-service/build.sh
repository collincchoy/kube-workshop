#! /bin/sh
poetry export -f requirements.txt > requirements.txt
docker build -t kube-workshop-cronkite:v1 .
