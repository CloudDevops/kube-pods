Python file, Dockerfile and requirements.txt are included. 

pip install -r requirements.txt

#build the Dockerfile

docker build -t k8s-python-app .

#helm commands

helm create k8s-python-app

helm install k8s-python-app ./k8s-python-app
