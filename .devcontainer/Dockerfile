# continuumio/anaconda3

FROM --platform=linux/arm64 debian:12
RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install rsync zip openssh-server
RUN apt-get -y install cmake git tmux
RUN apt-get -y install curl
RUN apt-get -y install wget
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential libffi-dev libssl-dev
# build-base=0.5-r3
RUN apt-get clean
# COPY src/ /app/src
# COPY test/ /app/test
# COPY run.sh /app/
# COPY build_run.sh /app/
# COPY test.sh /app/
# COPY build_run_test.sh /app/
# COPY CMakeLists.txt /app/
# WORKDIR /app
# RUN make -C src clean

