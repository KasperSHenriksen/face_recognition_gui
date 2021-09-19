FROM nvidia/cuda:11.4.1-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y \
    git \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    python3 \
    python3-pip \
    gcc \
    python3-tk \
    ffmpeg \
    libopenblas-dev \ 
    liblapack-dev

# Install dlib
RUN git clone https://github.com/davisking/dlib.git && \
    cd dlib && \
    mkdir build && \
    cd build && \
    cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1 && \
    cmake --build . && \
    cd .. && \
    python3 setup.py install 

# Install Face Recognition and OpenCV
RUN pip3 install face_recognition opencv-python

WORKDIR /face_recognition/app