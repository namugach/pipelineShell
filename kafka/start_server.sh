#!/bin/bash

cd /home/ubuntu/app/kafka/kafka_2.13-3.6.2/

nohup ./bin/kafka-server-start.sh config/server.properties >/dev/null 2>&1 &
