#!/bin/bash

/root/app/kafka/kafka_2.13-3.6.2/bin/zookeeper-server-stop.sh
/root/app/kafka/kafka_2.13-3.6.2/bin/kafka-server-stop.sh

sudo pkill -f kafka