docker-build:
	docker build -t fernandoe/fe-conta-server:local .

compose-bash:
	docker-compose run --rm conta /bin/sh

compose-build:
	docker-compose build conta

compose-up:
	docker-compose up conta

compose-stop:
	docker-compose stop

compose-rm:
	docker-compose rm

compose-migrate:
	docker-compose run --rm conta python manage.py migrate

compose-createsuperuser:
	docker-compose run --rm conta python manage.py createsuperuser

install-local-dependencies:
	pip install -e ../django-fe-jwt/

#docker-run:
#	docker run --rm -p 80:8000 -d fernandoe/fe-conta-server
#
#kube-server:
#	kubectl create -f k8s/server.yaml
#
#kube-get-pods:
#	kubectl get pods -o wide
#
#kube-get-svc:
#	kubectl get svc
#
#kube-expose-fe-conta:
#	kubectl expose deployment fe-conta --type=NodePort
#
#minikube-start:
#	minikube start --docker-env http_proxy=http://15.85.195.199:8088 --docker-env https_proxy=http://15.85.195.199:8088 --docker-env no_proxy=192.168.99.0/24
#
#minikube-open:
#	minikube service fe-conta
#
#watch-get-pods:
#	watch kubectl get pods
#
#machine-create:
#	docker-machine create --driver virtualbox default
#
#machine-default:
#	eval $(docker-machine env default)
#
