#!/bin/bash

# .env 파일 로드
DIR_PATH=$(realpath .)
source $DIR_PATH/.env

# Docker 명령어 실행
docker compose down
docker container rm ${IMAGE_NAME}:${IMAGE_VERSION}
docker image rm ${IMAGE_NAME}:${IMAGE_VERSION}