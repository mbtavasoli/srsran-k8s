ARG OS_VERSION=24.04

FROM ubuntu:$OS_VERSION AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    cmake \
    build-essential \
    make \
    gcc \
    g++ \
    pkg-config \
    libfftw3-dev \
    libmbedtls-dev \
    libsctp-dev \
    libyaml-cpp-dev \
    libgtest-dev \
    libboost-program-options-dev \
    libconfig++-dev \
    libzmq3-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone https://github.com/srsRAN/srsRAN_4G.git

RUN cd srsRAN_4G && mkdir build && cd build && \
    cmake ../  && \
    make
