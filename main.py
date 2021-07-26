""" module path for search by python interpreter
import sys
print(sys.path)
"""

from configs import logConfig
from person.manager.personManager import PersonManager
from videos.manager.videoManager import VideoManager
from resources.resource import resources_configs

if __name__ == '__main__':
    """ the entry point of program """
    logConfig.config()
    #VM1 = VideoManager(3, "192.168.0.99", 9998, "HD720")
    #VM1.start()
    PM1 = PersonManager(1, "192.168.0.99", 9999)
    #PM2 = PersonManager(30, "192.168.0.99", 9999)
    PM1.start()
    #PM2.start()
    #PM3 = PersonManager(1, "192.168.0.99", 9999)
    #PM3.start()
    print('Main Finish')




