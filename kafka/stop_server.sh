#!/bin/bash

/home/ubuntu/app/kafka/kafka_2.13-3.6.2/bin/zookeeper-server-stop.sh
/home/ubuntu/app/kafka/kafka_2.13-3.6.2/bin/kafka-server-stop.sh

sudo pkill -f kafka