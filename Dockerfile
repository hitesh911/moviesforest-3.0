FROM python:3.9.2-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


CMD ["waitress-serve","--port=8000","movie_forest.wsgi:application"]
