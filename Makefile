TRAVIS_REPO_SLUG ?= fernandoe/fe-conta-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	true
#	cd src; pytest -s

travis.test:
	true
#	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
