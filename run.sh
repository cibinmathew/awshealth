#!/bin/sh)

docker build -t flask-aws .
docker run --rm -d -p 5000:5000 flask-aws