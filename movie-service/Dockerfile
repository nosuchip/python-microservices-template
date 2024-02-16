FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY ./requirements.txt /app/requirements.txt

COPY ./shared_dist/*.whl /shared_dist/

RUN pip install  /shared_dist/*.whl

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip /shared_dist/

COPY . /app/
