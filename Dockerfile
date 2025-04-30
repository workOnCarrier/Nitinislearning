
FROM --platform=linux/arm64 debian:10
RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install rsync zip openssh-server
RUN apt-get -y install cmake
RUN apt-get clean
COPY src/ /app/src
COPY test/ /app/test
COPY run.sh /app/
COPY build_run.sh /app/
COPY test.sh /app/
COPY build_run_test.sh /app/
COPY CMakeLists.txt /app/
WORKDIR /app
RUN make -C src clean
