#!/bin/bash

for file in *;
do
        echo "Stopping Docker container"
        sudo docker stop python-container
	sudo docker rm python-container
        echo "Goodbye!"
done
