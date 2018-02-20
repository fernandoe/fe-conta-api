docker-build:
	docker build -t fernandoe/fe-conta .

docker-run:
	docker run --rm -p 80:8000 -d fernandoe/fe-conta
