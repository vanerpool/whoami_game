FROM python:3.8-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN pip install poetry==1.1.11
ENV PATH="${PATH}:/root/.poetry/bin"

# set work directory
WORKDIR /app

# copy project
COPY . .

# install poetry deps
RUN poetry install
