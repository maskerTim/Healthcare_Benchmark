import os

def getResources():
    fileend = [".mp4"]
    dirpath = os.path.dirname(__file__)
    return [os.path.join(dirpath, _) for _ in os.listdir(dirpath) if os.path.splitext(_)[1] in fileend ]

resources_config = {
    "files": getResources()
}