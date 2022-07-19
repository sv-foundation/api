FROM python:3.10-buster
# RUN apt-get update && apt-get -y upgrade && apt-get -y install build-essential cmake
WORKDIR /app
# COPY requirements/. requirements/
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
RUN chmod +x /app/entrypoint.sh

RUN useradd -m -s /bin/bash usr && chown -R usr:usr /app
USER usr
