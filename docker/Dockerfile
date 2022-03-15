# pull the official base image
FROM python:3.10.2

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY env/requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY project /usr/src/app

# set up database
RUN rm -rf db.sqlite3
RUN python manage.py migrate 
RUN python manage.py insert_fakedata --superuser 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]