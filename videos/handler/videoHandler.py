from ..videoFactory import VideoFactory
import logging
import time
import pickle
import struct
import datetime

class VideoHandler:
    """
    Create some video for healthcare by factory and Operate it
    """
    def __init__(self, video="US"):
        self.videoHandler = VideoFactory(video)

    """ Open the video and Record it"""
    def openAndRecordVideo(self, file, type="file"):
        start = datetime.datetime.now()
        cap = self.videoHandler.open(file, type)
        while True:
            flag, frame = cap.read()
            if flag:
                frame = pickle.dumps(frame)
                p = struct.pack('I', len(frame))
                frame = p + frame
                self.videoHandler.recordVideo(frame)
            # break down the recording video
            end = datetime.datetime.now()
            if (end-start).seconds > 30:
                break

    """ Play the video """
    def play(self, ID, ip, port):
        try:
            # set process ID as identification
            self.videoHandler.setID(ID)
            # connect the server/host
            self.videoHandler.connect(ip, port)
            # play the video
            for f in self.videoHandler.frames:
                self.videoHandler.sendall(f)
        except Exception as e:
            logging.error("Error: {}".format(e))
        finally:
            time.sleep(3)
            self.videoHandler.close()
            logging.info("Video is closed...")