# Dockerizing_Django(DD)

DD project started merely for learning django, docker and etc. But now, the intention is changing like follows.

## Target users

Target users vary depending on a branch.
### Master (General)
For those of you who want to learn or use django, docker, etc for their whatever project.

### Celery-redis (Machine learning oriented)
For AI engineer/data scientists who knows how to make models and stuff but don't know how to deploy API.

## Usage

```bash
docker-compose up
```
Delete existing volume to refresh static data(restframework)
```bash
docker-compose down -v
```
Do this again to start container
```bash
docker-compose up
```

Access to the link below to see api

```
localhost:80/api
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## System structure
### Master
WebFramework: Django
DB: PostgreSQL
WebServer: Nginx
(ApplicationServer: Gunicorn)

### celery_redis
Basic structure + celery + redis
For asynchronous task queue/job queue
