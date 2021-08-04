from .video import Video
import cv2

class Camera(Video):
    """ Camera Simulator """
    def openVideoFile(self, filepath):
        """ open the video file
        @param {filepath: the path of video file}
        """
        # open the video file
        cap = cv2.VideoCapture(filepath)
        # get the position/index of frame in this video
        # pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap = cap
