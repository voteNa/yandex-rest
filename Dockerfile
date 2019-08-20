FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

# install dependencies
RUN apk update --no-cache && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip3 install --no-cache-dir -r requirements.txt


COPY ./server /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "app"]