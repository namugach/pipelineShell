#!/bin/bash

docker run -itd \
  --name server2 \
  --hostname server1 \
  --add-host server1:172.31.14.186 \
  --add-host server2:172.31.1.229 \
  --add-host server3:172.31.10.99 \
  -p 2222:2222 \
  namugach/ubuntu-pipeline:24.04-kafka-test