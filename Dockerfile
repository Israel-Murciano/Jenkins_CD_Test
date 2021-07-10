FROM ubuntu:latest
USER root
ENV VERSION=1.5.0
RUN apt-get update -y && apt-get install -y \
    python \
    vim \
    zip \
    unzip
COPY job.py /tmp
CMD uname -a && [ -f /tmp/job.py ] && echo "File exist" || echo "File does not exist"