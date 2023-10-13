FROM debian:12
RUN apt-get update && apt-get -y install dpkg-dev dh-exec \
dh-python python3-setuptools python3-twisted python3-requests
