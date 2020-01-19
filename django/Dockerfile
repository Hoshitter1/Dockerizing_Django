FROM python:3.7.2

#TODO Not sure which dir is the best for this project yet
ENV APP_PATH /opt/apps

COPY . $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt
#For postgre
RUN pip install psycopg2
#For debugging
RUN apt update && apt install -y vim

WORKDIR $APP_PATH
#TODO delete pwd later
RUN pwd
#RUN $APP_PATH/wait-for-it.sh db:5432
RUN python manage.py collectstatic --noinput
