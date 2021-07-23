import threading
from ..handler.videoHandler import VideoHandler
from resources.resource import resources_configs
import logging
import pickle
import struct

class VideoManager(threading.Thread):
    """ Manager the video"""
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
        for _ in range(self.number):
            videoUS = VideoHandler('CAM')
            self.videos.append(videoUS)
        logging.info('Succeed to create videos')

    def connect(self):
        for v in self.videos:
            v.connectTo(self.ip, self.port)

    def run(self):
        payloadSize = 'I'
        self.createVideos()
        logging.info("open the video...")
        cap = VideoHandler.open(resources_configs["files"](self.resolution)[0])
        logging.info("connect the server/host")
        self.connect()
        try:
            no_flag_count = 0
            while True:
                flag, frame = cap.read()
                if flag:
                    no_flag_count = 0
                    car_count = VideoHandler.detectCar(frame)
                    logging.info("car count:{}".format(car_count))
                    frame = pickle.dumps(frame)
                    p = struct.pack(payloadSize, len(frame))
                    frame = p + frame
                    for v in self.videos:
                        t = threading.Thread(target=v.sendAll, args=(frame,))
                        self.threadManager.append(t)
                        t.start()
                    for t in self.threadManager:
                        t.join()
                else:
                    no_flag_count+=1
                if no_flag_count > 5:
                    break
            logging.info("Finish to send the video")
        except Exception as e:
            logging.error("send error...maybe connection is broken or other fault occurs")
            logging.error(e)
        finally:
            for v in self.videos:
                v.close()
