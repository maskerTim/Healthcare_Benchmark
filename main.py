import sys
print(__name__)
print(sys.path)

import threading
from configs import logConfig
from person.manager.personManager import PersonManager

if __name__ == '__main__':
    logConfig.config()
    PM1 = PersonManager(1, "192.168.100.60", 9998)
    #PM2 = PersonManager(50, "192.168.100.70", 9999)
    PM1.start()
    #PM2.start()
    PM1.join()
    #PM2.join()
    print(threading.enumerate())
    print('Main Finish')




