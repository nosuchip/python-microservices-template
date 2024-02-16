#!/bin/sh

pushd ./movie-service
pipenv lock
pipenv sync
pipenv run pip freeze > requirements.txt
popd

pushd ./cast-service
pipenv lock
pipenv sync
pipenv run pip freeze > requirements.txt
popd
