FROM python:3.9.2

WORKDIR /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["waitress-serve","--port=8000 movie_forest.wsgi:application"]
