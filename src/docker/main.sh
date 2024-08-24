#!/bin/bash

service ssh start
service mysql start
envsubst < /src/docker/settings/kafka/server.properties > /root/app/kafka/kafka_2.13-3.6.2/config/server.properties
envsubst < /src/docker/settings/kafka/zookeeper.properties > /root/app/kafka/kafka_2.13-3.6.2/config/zookeeper.properties
echo ${BRKER_ID} > /root/zkdata/myid 

sleep infinity