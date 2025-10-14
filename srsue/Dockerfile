# =========================
# srsRAN UE Multi-Stage Dockerfile
# =========================

ARG OS_VERSION=24.04

# =========================
# Stage 1: Build Stage
# =========================
FROM ubuntu:${OS_VERSION} AS builder

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
    CXXFLAGS="-Wno-error=array-bounds" cmake ../ -DBUILD_TESTING=OFF && \
    make -j$(nproc) install

# =========================
# Stage 2: Runtime Stage
# =========================
FROM ubuntu:${OS_VERSION}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    libfftw3-dev \
    libmbedtls-dev \
    libsctp-dev \
    libyaml-cpp-dev \
    libboost-program-options-dev \
    libconfig++-dev \
    libzmq3-dev \
    iproute2 \
    python3 \
    tmux \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local
COPY --from=builder /opt/srsRAN_4G /opt/srsRAN_4G
