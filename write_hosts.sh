#!/bin/bash

IP_FORMAT_STRING="{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}"
NAMES=("cd" 
  "swarm-node2" 
  "swarm-node1")
for name in ${NAMES[@]}; do
  IP=`docker inspect --format "$IP_FORMAT_STRING" devops_$name\_1`;
  echo $IP
done;

