#!/bin/bash
xhost +
docker run --gpus all --device /dev/nvidia0 --device /dev/nvidia-uvm --device /dev/nvidia-uvm-tools \
           --device /dev/nvidiactl \
           -it \
           --rm \
           -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
           -v $(pwd):/face_recognition \
           --device=/dev/video0:/dev/video0 \
           face_recognition
xhost -