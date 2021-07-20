from ..videoFactory import VideoFactory
import logging
import time
import pickle
import struct

class VideoHandler:
    """
    Create some video for healthcare by factory and Operate it
    """
    def __init__(self, video="US"):
        self.videoHandler = VideoFactory(video)

    def play(self, ID, ip, port, filepath, type='file'):
        try:
            # connect the server/host
            self.videoHandler.connect(ip, port)
            # open the video resource
            print(filepath)
            cap = self.videoHandler.open(ID, type, filepath)
            while True:
                flag, frame= cap.read()
                if flag:
                    frame = pickle.dumps(frame)
                    p = struct.pack('I', len(frame))
                    frame = p + frame
                    self.videoHandler.sendall(frame)
        except Exception as e:
            logging.error(e)
            #logging.error("Error connection exception...")
        finally:
            time.sleep(3)
            self.videoHandler.close()
            logging.info("video is closed...")