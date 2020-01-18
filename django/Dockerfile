FROM python:3.7.2

ENV APP_PATH /opt/apps

COPY . $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt
RUN pip install psycopg2

WORKDIR $APP_PATH
#TODO delete pwdß later
RUN pwd
RUN $APP_PATH/wait-for-it.sh db:5432
RUN python manage.py collectstatic --noinput
