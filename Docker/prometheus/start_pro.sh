#!/bin/bash

docker rm -f prometheus
docker run --name=prometheus -d -p 9090:9090 -v $(pwd)/prometheus.yml:/usr/tmp/prometheus/prometheus.yml prom/prometheus