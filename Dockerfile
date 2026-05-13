## We're making a Docker image that is like a portable Linux computer with Python, our app's dependencies,
## and the AWS CLI all pre-installed — so that wherever this image runs
## (locally or on an AWS server), it has everything it needs to work.

FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y --no-install-recommends awscli

RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "app.py"]