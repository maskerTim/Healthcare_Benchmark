from .models.camera import Camera

def VideoFactory(video):
    """ Factory for making video gadgets """
    videos = {
        "CAM": Camera()
    }
    return videos[video]