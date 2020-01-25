
DB_USERNAME := user_dev
DB_NAME := develop_db

database: #See what's in database
	docker exec -it postgres_db bash -c "psql -U $(DB_USERNAME) -d $(DB_NAME)"

web: #See what's in django
	docker exec -it django_container bash

ws: #See what's in webserver
	docker exec -it nginx_django bash