#!/bin/sh

pushd ./shared
pipenv lock
pipenv sync
pipenv run pip freeze > requirements.txt

pipenv install --dev
pipenv run python -m build
popd

pushd ./movie-service
pipenv lock
pipenv sync
pipenv run pip freeze | grep -v python-microservices-shared > requirements.txt
mkdir -p shared_dist
cp ../shared/dist/*.whl shared_dist/
popd

pushd ./cast-service
pipenv lock
pipenv sync
pipenv run pip freeze | grep -v python-microservices-shared > requirements.txt
mkdir -p shared_dist
cp ../shared/dist/*.whl shared_dist/
popd

docker compose build