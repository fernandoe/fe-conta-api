TRAVIS_REPO_SLUG ?= fernandoe/fe-conta-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

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
