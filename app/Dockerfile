FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade -r requirements.txt
