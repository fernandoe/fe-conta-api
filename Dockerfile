FROM fernandoe/docker-python:3.6.5-alpine

ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD ./docker/run.sh /run.sh
ADD ./src /app

WORKDIR /app

CMD ["/run.sh"]
