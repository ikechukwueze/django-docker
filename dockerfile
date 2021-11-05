# pull the official base image
FROM python:3.8.12-bullseye

# set work directory
WORKDIR /usr/project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/project
RUN pip install -r requirements.txt

# copy project into docker container's work directory
COPY . /usr/project