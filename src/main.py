import threading
from configs import logConfig
from person.manager.personManager import PersonManager

if __name__ == '__main__':
    logConfig.config()
    PM = PersonManager(1)
    PM.start()
    PM.join()
    print(threading.enumerate())
    print('Main Finish')




