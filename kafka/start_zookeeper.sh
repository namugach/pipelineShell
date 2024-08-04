#!/bin/bash

cd /home/ubuntu/app/kafka/kafka_2.13-3.6.2/

nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties >/dev/null 2>&1 &
