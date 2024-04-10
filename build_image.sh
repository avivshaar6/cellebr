#!/bin/bash

docker build -t server:latest .
docker tag server:latest aviv012/server:latest
docker push aviv012/server:latest