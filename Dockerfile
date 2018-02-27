FROM python:3.6.4-alpine

RUN apk add --no-cache build-base mariadb-client-libs

RUN apk add --no-cache --virtual .build-deps mariadb-dev

ADD ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN apk del .build-deps

ADD ./docker/run.sh /run.sh
ADD ./src /app

WORKDIR /app

CMD ["/run.sh"]

# Use this to build MySQL-Client
# https://github.com/gliderlabs/docker-alpine/issues/181
