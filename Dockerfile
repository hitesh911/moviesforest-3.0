FROM python:3.8.0-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY example /usr/src/app/
COPY entrypoint.sh /usr/src/app

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
