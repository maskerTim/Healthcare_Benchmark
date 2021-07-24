import logging
import os

""" the dictionary search of video resolution path"""
video_resolution = {
    "HD1080": os.path.join(os.path.dirname(__file__), 'HD1080'),
    "HD720": os.path.join(os.path.dirname(__file__), 'HD720')
}

def getResources(resolution="HD1080"):
    """ get the vidoe file resource
    @param {resolution: the resolution of video file}
    @return the path of the resolution of video file
    """
    fileend = [".mp4"]
    dirpath = video_resolution[resolution]
    logging.info("Resource Path:{}, Resolution:{}".format(dirpath, resolution))
    return [os.path.join(dirpath, _) for _ in os.listdir(dirpath) if os.path.splitext(_)[1] in fileend]

def getModel():
    """ get the classifier model (e.g., car classifier model)"""
    fileend = [".xml"]
    dirpath = os.path.join(os.path.dirname(__file__))
    logging.info("Model Path:{}".format(dirpath))
    return [os.path.join(dirpath, _) for _ in os.listdir(dirpath) if os.path.splitext(_)[1] in fileend]

""" the dictionary search of the functionalities """
resources_configs = {
    "files": getResources,
    "models": getModel
}