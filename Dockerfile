FROM python:3

LABEL MAINTAINER JKOUSSAWO

ENV PYTHONUNBUFFERED 1

ADD . /mypass

WORKDIR /mypass

COPY ./requirements.txt /mypass/requirements.txt 

RUN pip install -r requirements.txt

COPY . /app
