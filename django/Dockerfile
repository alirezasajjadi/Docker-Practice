FROM docker.arvancloud.ir/python:3.10

WORKDIR /django

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . . 