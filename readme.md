# Dockerizing_Django(DD)

DD is the repository to learn django and create a basic set of scripts to get started easily

## Usage

```bash
docker-compose up
```

#### To access
##### 1. Go to your browser
##### 2. Type [base url](localhost:80) in url bar
#### For django admin
[admin page](localhost:80/admin)

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