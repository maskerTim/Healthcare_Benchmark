# Healthcare_Benchmark
###### tags: `github` `benchmark` `healthcare`
## Introduction
This is a project for the benchmark of healthcare simulation.
## Prerequisites
### Development Tools
* Python 3.5+
* Docker

### Configuration File
#### .env
Please make the `.env` file to config the environment variable for this project.
```
IMAGE_NAME=[Docker Image of this program]
IMAGE_TAG=[Docker Image Tag]
MQTT_TOPIC_SENSOR_PREFIX=[Sensor Prefix Topic Name]
MQTT_TOPIC_VIDEO_PREFIX=[Video Prefix Topic Name]
MQTT_TOPIC_ACTUATOR_PREFIX=[Actuator Prefix Topic Name]
```
#### Dockerfile
Please make the `Dockerfile` file to make the docker image.<br>
The following is sample code:
```
FROM [Docker Python Base Image]

(Optional)
LABEL Maintainer=[Author Name] \
      Email=[Author Email] \
      Project=[Project Name] \
      Version=[Project Version]

RUN apt update && \
    apt install net-tools ffmpeg libsm6 libxext6  -y

RUN apt-get update \
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

WORKDIR /project

# Copy requirement.txt file in a container
COPY ./requirement.txt .

RUN pip install -r requirement.txt

VOLUME ["/project"]

(Optional)
CMD ["bash"]
```
#### (Optional)docker-compose.yml
Please make the `docker-compose.yml` file to automatically run multiple containers.
```
version: "3.9"
services:
  [Container Name]:
    image: "${IMAGE_NAME}:${IMAGE_TAG}"
    container_name: [Container Name]
    stdin_open: true
    tty: true
    volumes:
      - "${HOST_VOLUME}:${CONTAINER_VOLUME}"
    command: python main.py
    networks:
      - network-1
  [Container Name]:
    image: "${IMAGE_NAME}:${IMAGE_TAG}"
    container_name: [Container Name]
    stdin_open: true
    tty: true
    volumes:
      - "${HOST_VOLUME}:${CONTAINER_VOLUME}"
    command: python main.py
    networks:
      - network-2
  ...
networks:
  network-1:
    external:
      name: [Docker Network Name]
  network-2:
    external:
      name: [Docker Network Name]
  [Network Name]:
    external:
      name: [Docker Network Name]

```