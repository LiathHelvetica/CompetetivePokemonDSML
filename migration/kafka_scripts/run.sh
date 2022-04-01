#!/bin/bash

KAFKA_HOME="/home/liath/Kafka"

cd ${KAFKA_HOME} || exit

nohup bin/zookeeper-server-start.sh config/zookeeper.properties &
sleep 2

nohup bin/migration-server-start.sh config/server.properties &
sleep 2

docker run -d --network=host -p 8080:8080 -e KAFKA_BROKERS=localhost:20300 quay.io/cloudhut/kowl:master