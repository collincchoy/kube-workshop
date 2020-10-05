#! /bin/sh
docker tag kube-workshop-flask-web collincchoy/kube-workshop-flask-web
docker push collincchoy/kube-workshop-flask-web
docker tag kube-workshop-cronkite collincchoy/kube-workshop-cronkite
docker push collincchoy/kube-workshop-cronkite