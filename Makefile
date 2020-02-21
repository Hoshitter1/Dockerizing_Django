
DB_USERNAME := user_dev
DB_NAME := develop_db

database: #See what's in database
	docker exec -it postgres_db bash -c "psql -U $(DB_USERNAME) -d $(DB_NAME)"

web: #See what's in django
	docker-compose run django bash

ws: #See what's in webserver
	docker-compose run nginx bash

shell: #Going into django shell (Use this when debugging or when you forget your password and stuff)
	docker-compose run --rm django sh -c "sleep 1 && python /opt/apps/manage.py shell"

loaddata: #Read initial data
	docker-compose run --rm django sh -c "python manage.py loaddata init_user.json"

delete_migrate: #[BE CAREFUL] this deletes all migration history so that you can test various model structures
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
