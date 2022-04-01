#!/bin/bash

KAFKA_HOME="/home/liath/Kafka"

cd ${KAFKA_HOME} || exit

bin/migration-server-stop.sh
bin/zookeeper-server-stop.sh