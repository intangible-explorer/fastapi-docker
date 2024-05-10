FROM python:3.9

WORKDIR /fastapi-app

COPY requirements.txt /fastapi-app/

RUN pip install -r requirements.txt

COPY . /fastapi-app/