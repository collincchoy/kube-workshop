#! /bin/sh
docker run -it --rm -p 8000:8000 kube-workshop-cronkite:v1 --host 0.0.0.0 $@
