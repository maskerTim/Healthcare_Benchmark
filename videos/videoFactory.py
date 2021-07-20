from .models.ultrasound import Ultrasound

def VideoFactory(video):
    """ Factory for making sensors """
    videos = {
        "US": Ultrasound()
    }
    return videos[video]