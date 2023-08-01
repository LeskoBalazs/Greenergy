#!/bin/bash

for file in *;
do
        echo "Starting built Docker image"
        sudo docker run -d --name python-container -p 8000:8000 python-app
        echo "Docker image has been started"
done

