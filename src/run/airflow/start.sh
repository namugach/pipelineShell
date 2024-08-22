#!/bin/bash

nohup airflow webserver --port 8880 > ~/airflow/logs/webserver.log 2>&1 &

airflow scheduler
