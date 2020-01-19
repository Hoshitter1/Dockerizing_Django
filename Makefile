
DB_USERNAME := user_dev
DB_NAME := develop_db

database: #See what's in database
	docker exec -it postgres_db bash -c "psql -U $(DB_USERNAME) -d $(DB_NAME)"

api: #See what's in database
	docker exec -it django_container bash