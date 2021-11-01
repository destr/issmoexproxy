FROM debian:9
RUN apt-get update && apt-get -y install dpkg-dev dh-exec \
python3-setuptools python3-twisted python3-requests
