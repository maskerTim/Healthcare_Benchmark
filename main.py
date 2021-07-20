""" module path for search by python interpreter
import sys
print(sys.path)
"""

from configs import logConfig
from person.manager.personManager import PersonManager

if __name__ == '__main__':
    logConfig.config()
    PM1 = PersonManager(100, "192.168.0.99", 9999)
    PM2 = PersonManager(100, "192.168.0.99", 9999)
    PM1.start()
    PM2.start()
    #PM3 = PersonManager(1, "192.168.0.99", 9999)
    #PM3.start()
    print('Main Finish')




