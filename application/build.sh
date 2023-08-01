#!/bin/bash

for file in *;
do
	echo "Building Docker image for Python app"
	sudo docker build -t python-app .
	echo "Docker image has been built, ready to start"
done
