#!/bin/bash

KAFKA_HOME="/home/liath/Kafka"

cd ${KAFKA_HOME} || exit

nohup bin/zookeeper-server-start.sh config/zookeeper.properties &
sleep 5

nohup bin/kafka-server-start.sh config/server.properties &
sleep 5

docker run -d --network=host -p 20301:20301 -e KAFKA_BROKERS=localhost:20300 quay.io/cloudhut/kowl:master

bin/kafka-topics.sh --create --topic pokemon-export --bootstrap-server localhost:20300