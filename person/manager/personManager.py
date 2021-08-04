""" import module path
print(__name__)
"""

from sensors.group.sensorGroup import Person
from multiprocessing import Pool
import os
import threading


class PersonManager(threading.Thread):
    """ Manage the person instance """
    def __init__(self, number=1, ip="0.0.0.0", port=9999):
        threading.Thread.__init__(self)
        self.people = []
        self.number = number
        self.ip = ip
        self.pool = Pool(os.cpu_count())
        self.port = port

    def createPerson(self):
        """ multithreading version for creating the person instance"""
        for _ in range(self.number):
            self.people.append(threading.Thread(target=Person(self.ip, self.port).operate))

    def getPeople(self):
        """ get the all person instances """
        return self.people

    def run(self):
        """ running all person instances """
        # ----- multiprocessing version -----
        # [self.pool.apply_async(func=Person(self.ip, self.port).operate, args=(4,)) for _ in range(self.number)]
        # self.pool.close()
        # self.pool.join()
        # ----- multithreading version -----
        self.createPerson()
        if self.people:
            [p.start() for p in self.people]



