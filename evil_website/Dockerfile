# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy contents from the local file to the image
COPY . /app

# $env:FLASK_APP = 'project'
ENV FLASK_APP='project' 

# $env:FLASK_DEBUG = '1'
ENV FLASK_DEBUG='1' 

ENTRYPOINT flask run --host=0.0.0.0 --port=4000