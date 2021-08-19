import threading

import cv2

from ..handler.videoHandler import VideoHandler
from resources.resource import resources_configs
import logging
import base64
import os
import time


class VideoManager(threading.Thread):
    """ Manager the video instances"""

    def __init__(self, name, number, ip, port, resolution="HD1080"):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.number = number
        self.name = name
        self.resolution = resolution
        self.videos = []
        self.threadManager = []

    def createVideos(self, video):
        """ create the video instances """
        for _ in range(self.number):
            self.videos.append(VideoHandler(video))
        logging.info('Succeed to create videos')

    def connect(self):
        """ connect to remote server/host """
        for v in self.videos:
            v.connectTo(self.ip, self.port, "mqttPub")

    def run(self):
        """ playing the video and send to remote server/host """
        self.connect()
        logging.info("connect the server/host")
        while True:
            cap = VideoHandler.open(resources_configs["files"](self.resolution)[0])
            logging.info("open the video...")
            try:
                while True:
                    flag, frame = cap.read()
                    if flag:
                        _, buffer = cv2.imencode('.jpg', frame)
                        # Converting into encoded bytes
                        jpg_as_text = base64.b64encode(buffer)
                        for v in self.videos:
                            v.sendAll("{}/{}".format(os.getenv("MQTT_TOPIC_VIDEO_PREFIX"), self.name), jpg_as_text)
                    else:
                        break
                # logging.info("Finish to send the video")
            except Exception as e:
                logging.error("send error...maybe connection is broken or other fault occurs")
                logging.error(e)
            finally:
                cap.release()
                for v in self.videos:
                    v.close()
            time.sleep(7)
