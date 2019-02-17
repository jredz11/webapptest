#!/usr/bin/env bash


docker cp ./jenkins/scripts/* `docker ps -q -l`:/tmp/*

python /tmp/EDAS.py $JENKINS_HOME/workspace/webapptest/target/webapptest.war
