DC?=docker-compose
CONTAINER?=back

.PHONY: help
help:
	@echo "\
Usage: \n\
    make up            Поднять приложение с нуля\n\
    make migrate       Выполнить миграции на БД\n\
    "

.PHONY: up
up:
	${DC} pull
	${DC} up --build -d
	make migrate

.PHONY: down
down:
	${DC} down

.PHONY: migrate
migrate:
	${DC} exec -T ${CONTAINER} sh -c "flask db init  || true"
	${DC} exec -T ${CONTAINER} sh -c "flask db migrate"
	${DC} exec -T ${CONTAINER} sh -c "flask db upgrade"