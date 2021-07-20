from ..videoFactory import VideoFactory
import logging
import time
import pickle
import struct
import threading

class VideoHandler:
    """
    Create some video for healthcare by factory and Operate it
    """
    def __init__(self, video="US"):
        self.videoHandler = VideoFactory(video)

    def play(self, ID, ip, port, filelist, type='file'):
        try:
            # connect the server/host
            self.videoHandler.connect(ip, port)
            # open the video resource
            for file in filelist:
                threading.Thread(target=self.playingbyvolumn, args=(ID, file, type)).start()

        except Exception as e:
            logging.error(e)
            #logging.error("Error connection exception...")
        finally:
            time.sleep(3)
            self.videoHandler.close()
            logging.info("video is closed...")

    def playingbyvolumn(self, ID, file, type):
        cap = self.videoHandler.open(ID, type, file)
        while True:
            flag, frame = cap.read()
            if flag:
                frame = pickle.dumps(frame)
                p = struct.pack('I', len(frame))
                frame = p + frame
                self.videoHandler.sendall(frame)