FROM python:3.6.4-alpine

WORKDIR /app

ADD ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ADD ./src /app

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
