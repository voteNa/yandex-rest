# toystory [Yandex Backend School] REST-api server

## Requirements
Python 3.5.2+
connexion[swagger-ui] == 2.3.0
flask-sqlalchemy == 2.4.0
flask-migrate == 2.5.2
psycopg2-binary==2.7.7
uwsgi

## Running with Docker-compose

To run the server on a Docker container, please execute the following from the root directory:
if docker run as root, need use sudo
```
make up
make migrate
```

and open your browser to here:

```
http://0.0.0.0:8080/ui/
```
