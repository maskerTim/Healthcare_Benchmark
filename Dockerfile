FROM python:3.8.0

LABEL Maintainer="MaskerTim" \
      Email="t109598001@ntut.org.tw" \
      Project="Healthcare Benchmark" \
      Version="1.0"

RUN apt update && \
    apt install net-tools ffmpeg libsm6 libxext6  -y

RUN apt-get --allow-releaseinfo-change update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

WORKDIR /project

# Copy healthcare directory into container's project directory
# COPY . .
COPY ./requirement.txt .

RUN pip install -r requirement.txt

VOLUME ["/project"]
