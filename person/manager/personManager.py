""" import module path
print(__name__)
"""

from ..person import Person
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

    """ multithreading version for creating the person instance"""
    def createPerson(self):
        for _ in range(self.number):
            self.people.append(threading.Thread(target=Person(self.ip, self.port).operate, args=()))

    def getPeople(self):
        return self.people

    def run(self):
        # multiprocessing version
        [self.pool.apply_async(Person(self.ip, self.port).operate, args=(_, )) for _ in range(self.number)]
        self.pool.close()
        self.pool.join()
        """
        # multithreading version
        self.createPerson()
        if self.people:
            [p.start() for p in self.people]
        """

