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
CONTAINER_VOLUME=/project
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

# How to start
1. Please build the dockerfile first.
    * `docker build -t $your_tag_name . $your_image_name` 
2. Set your environment variable in `.env`.
3. Change your ip address and port according your network configuration in `main.py`.
    * sample code
        ```
        sensorHR = SensorFactory('HR')
        sensorHR.setInterval(5)
        sensorBP = SensorFactory('BP')
        sensorBP.setInterval(3)
        patient1 = SensorGroup('Patient1', $your_ip, $your_port)
        patient1.setSensors([sensorHR, sensorBP])
        patient1.do()
        ```
4. Default network protocol is MQTT.
5. If you want to config different sensor attached with person, you can create a sensor by `SensorFactory` class. The sensor name is written in `SensorFactory` file. 
    * sample code
        ```
        sensor1 = SensorFactory($sensor_name)
        sensor1.setInterval(5)
        sensor2 = SensorFactory($sensor_name)
        sensor2.setInterval(3)
        patient1 = SensorGroup('Patient1', $your_ip, $your_port)
        patient1.setSensors([sensor1, sensor2])
        patient1.do()
        ```
    * SensorFactory class: `HR`-HeartRate, `BP`-BloodPressure, and `PO`-PulseOximeter are the different sensor type. 
        ```
        def SensorFactory(sensor):
            """ Factory for making sensors """
            sensors = {
                "HR": HeartRate(),
                "BP": BloodPressure(),
                "PO": PulseOximeter(),
                "FT": ForeheadTemperature()
            }
            return sensors[sensor]
        ```
6. The docker-compose can config by yourself, a container running can regard as person is detected the healthcare metrics by different healthcare sensors.
    * sample code
    ```
    version: "3.9"
    services:
      [Container Name]: # can be regarded as person
        image: "${IMAGE_NAME}:${IMAGE_TAG}" # set which image you want to use
        container_name: [Container Name] # set container name
        stdin_open: true
        tty: true
        volumes:    # host volume defaults './', and container volume defaults '/project' 
          - "${HOST_VOLUME}:${CONTAINER_VOLUME}"
        command: python main.py    # run a program
        networks:    # set virtual network for container
          - network-1
    ```
7. All configuration finish, let's run the application. Use `docker-compose up -d

# Contributor

| Name           |                 Agency                  |                Github                | Email                  |
| -------------- |:---------------------------------------:|:------------------------------------:| ---------------------- |
| Hao-Ying Cheng | National Taipei Unversity of Technology | [Link](https://github.com/maskerTim) | t109598001@ntut.org.tw |