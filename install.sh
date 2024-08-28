#!/bin/bash

DIR_PATH=$(realpath .)

source $DIR_PATH/.env

docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} $DIR_PATH/
docker compose up -d