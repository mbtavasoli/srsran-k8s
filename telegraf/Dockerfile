#=========================
# Telegraf Dockerfile for SRS
#=========================

ARG TELEGRAF_VERSION=1.35.0

FROM telegraf:${TELEGRAF_VERSION}

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends python3-websocket socat

ADD resources/telegraf.conf /etc/srs/

ADD resources/entrypoint.sh resources/ws_adapter.py /usr/local/bin/

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
