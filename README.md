import os
from kubernetes import client, configdef main():
config.load_kube_config()
v1 = client.CoreV1Api()
print("Listing pods with their status:")pod_status = os.getenv('POD_STATUS')

ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    if i.status.phase == pod_status:
        print("%s\\\\t%s\\\\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
if **name** == '**main**':
main()
Dockerfile

FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV POD_STATUS=Running

CMD [ "python", "./main.py" ]
requirements.txt

kubernetes==12.0.1

docker build -t k8s-python-app .

helm create k8s-python-app

helm install k8s-python-app ./k8s-python-app
