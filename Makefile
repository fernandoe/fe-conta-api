docker-build:
	docker build -t fernandoe/fe-conta-server .

docker-run:
	docker run --rm -p 80:8000 -d fernandoe/fe-conta-server

kube-server:
	kubectl create -f k8s/server.yaml

kube-get-pods:
	kubectl get pods -o wide

kube-get-svc:
	kubectl get svc
