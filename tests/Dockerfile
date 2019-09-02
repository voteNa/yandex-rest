FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

# install dependencies
RUN apk update --no-cache && \
#    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install --upgrade pip && pip3 install tox


COPY . /usr/src/app

EXPOSE 5001

ENTRYPOINT ["tox"]