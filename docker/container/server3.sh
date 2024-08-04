#!/bin/bash

source "/home/ubuntu/run/config.sh"

docker run -itd \
  --name $SERVER3_NAME \
  --hostname $SERVER3_NAME \
  --add-host $SERVER1_NAME:$SERVER1_IP \
  --add-host $SERVER2_NAME:$SERVER2_IP \
  --add-host $SERVER3_NAME:$SERVER3_IP \
  -p $SERVER2_PORT:$SERVER2_PORT \
  namugach/ubuntu-pipeline:24.04-kafka-test