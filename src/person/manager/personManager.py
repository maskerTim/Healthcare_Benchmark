from ..person import Person
import threading

class PersonManager(threading.Thread):
    """ Manage the person instance """
    def __init__(self, number=1):
        threading.Thread.__init__(self)
        self.people = []
        self.number = number

    def createPerson(self):
        for _ in range(self.number):
            self.people.append(threading.Thread(target=Person().operate, args=()))


    def getPeople(self):
        return self.people

    def run(self):
        self.createPerson()
        if self.people:
            [p.start() for p in self.people]

