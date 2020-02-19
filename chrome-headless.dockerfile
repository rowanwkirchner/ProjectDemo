#================================Base image=============================================================================
FROM selenium/standalone-chrome
USER root
#=================================Install Python========================================================================

ENV DEBIAN_FRONTEND=noninteractive \
    DEBCONF_NONINTERACTIVE_SEEN=true

RUN  echo "deb http://archive.ubuntu.com/ubuntu bionic main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu bionic-updates main universe\n" >> /etc/apt/sources.list \
  && echo "deb http://security.ubuntu.com/ubuntu bionic-security main universe\n" >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y \
    python-pip

RUN pip install toolium behave-webdriver --no-cache-dir



