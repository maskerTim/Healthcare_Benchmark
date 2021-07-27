import threading

import cv2

from ..handler.videoHandler import VideoHandler
from resources.resource import resources_configs
import logging
import base64
import pickle
import struct
import time

class VideoManager(threading.Thread):
    """ Manager the video instances"""
    def __init__(self, number=1, ip="0.0.0.0", port=9999, resolution="HD1080"):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.number = number
        self.resolution = resolution
        self.videos = []
        self.threadManager = []

    # def createAndRecordVideo(self):
    #     for _ in range(self.number):
    #         self.videoUS = VideoHandler('CAM')
    #         # open and record video in storage
    #         self.videoUS.openAndRecordVideo(resources_config["files"][0])
    #         self.addToManage(self.videoUS)
    #     logging.info("Finish to record")

    def createVideos(self):
        """ create the video instances """
        for _ in range(self.number):
            videoUS = VideoHandler('CAM')
            self.videos.append(videoUS)
        logging.info('Succeed to create videos')

    def connect(self):
        """ connect to remote server/host """
        for v in self.videos:
            v.connectTo(self.ip, self.port, "mqttPub")

    """ @deprecated """
    # def run(self):
    #     """ playing the video and send to remote server/host """
    #     payloadSize = 'I'
    #     self.createVideos()
    #     logging.info("open the video...")
    #     cap = VideoHandler.open(resources_configs["files"](self.resolution)[0])
    #     logging.info("connect the server/host")
    #     self.connect()
    #     try:
    #         #no_flag_count = 0
    #         while True:
    #             flag, frame = cap.read()
    #             if flag:
    #                 no_flag_count = 0
    #                 #car_count = VideoHandler.detectCar(frame)
    #                 #logging.info("car count:{}".format(car_count))
    #                 frame = pickle.dumps(frame)
    #                 p = struct.pack(payloadSize, len(frame))
    #                 frame = p + frame
    #                 for v in self.videos:
    #                     v.sendAll("Try/MQTT", frame)
    #                     #t = threading.Thread(target=v.sendAll, args=("Try/MQTT", frame,))
    #                     #self.threadManager.append(t)
    #                     #t.start()
    #                 time.sleep(0.5)
    #                 # for t in self.threadManager:
    #                 #     t.join()
    #         #logging.info("Finish to send the video")
    #     except Exception as e:
    #         logging.error("send error...maybe connection is broken or other fault occurs")
    #         logging.error(e)
    #     finally:
    #         for v in self.videos:
    #             v.close()

    def run(self):
        """ playing the video and send to remote server/host """
        self.createVideos()
        logging.info("open the video...")
        cap = VideoHandler.open(resources_configs["files"](self.resolution)[0])
        logging.info("connect the server/host")
        self.connect()
        try:
            while True:
                flag, frame = cap.read()
                if flag:
                    _, buffer = cv2.imencode('.jpg', frame)
                    # Converting into encoded bytes
                    jpg_as_text = base64.b64encode(buffer)
                    for v in self.videos:
                        v.sendAll("Try/MQTT", jpg_as_text)
            #logging.info("Finish to send the video")
        except Exception as e:
            logging.error("send error...maybe connection is broken or other fault occurs")
            logging.error(e)
        finally:
            cap.release()
            for v in self.videos:
                v.close()
