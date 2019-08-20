# toystory [Yandex Backend School] REST-api server

## Overview

## Requirements
Python 3.5.2+
connexion[swagger-ui] == 2.3.0
flask-sqlalchemy == 2.4.0
flask-migrate == 2.5.2
psycopg2-binary==2.7.7
uwsgi

## Usage
To run the server, please execute the following from the root directory[server]:

```
pip3 install -r requirements.txt
python3 -m app
```

and open your browser to here:

```
http://0.0.0.0:8080/ui/
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker-compose

To run the server on a Docker container, please execute the following from the root directory:

```bash
docker-compose up
```