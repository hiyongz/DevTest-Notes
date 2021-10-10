#!/bin/bash

docker rm -f holmes conan
docker run --name=conan -itd -p 8999:4200 conan
docker run --name=holmes -itd --net=container:conan holmes