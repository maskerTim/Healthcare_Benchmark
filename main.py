""" module path for search by python interpreter
import sys
print(sys.path)
"""

from configs import logConfig
from person.manager.personManager import PersonManager
from videos.manager.videoManager import VideoManager

if __name__ == '__main__':
    logConfig.config()
    VM1 = VideoManager(10, "192.168.0.99", 9998)
    VM1.start()
    #PM1 = PersonManager(3, "192.168.100.60", 9998)
    #PM2 = PersonManager(30, "192.168.100.60", 9998)
    #PM1.start()
    #PM2.start()
    #PM3 = PersonManager(1, "192.168.0.99", 9999)
    #PM3.start()
    print('Main Finish')




