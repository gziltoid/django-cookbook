FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y sudo vim && apt-get upgrade -y

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
