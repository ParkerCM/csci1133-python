from time import time
import random

class Bug():
    def __init__(self, initPos=0):
        self.position = initPos
        self.dirRight = True
    def move(self):
        if self.dirRight is True:
            self.position += 1
        else:
            if self.position == 0:
                self.position = 0
            else:
                self.position -= 1
    def turn(self):
        if self.dirRight is True:
            self.dirRight = False
        else:
            self.dirRight = True
    def display(self):
        if self.dirRight is True:
            self.direction = 'right'
            self.dirSign = '>'
        else:
            self.direction = 'left'
            self.dirSign = '<'
        print('position', self.position, ', direction', self.direction,\
        ':','.'*self.position, self.dirSign)

class Stopwatch():
    def __init__(self):
        self.__startTime = time()
        self.__endTime = time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def start(self):
        self.__startTime = time()
    def stop(self):
        self.__endTime = time()
    def elapsedTime(self):
        return self.__endTime - self.__startTime

def testA():
    count = 0
    b = Bug(10)
    b.display()
    b.move()
    b.display()
    b.turn()
    b.display()
    while count < 13:
        b.move()
        b.display()
        count += 1

def testB():
    time = Stopwatch()
    randList = [0]*10000
    count = 0
    while count < len(randList):
        randList[count] = random.randint(0, 1000000)
        count += 1
    time.start()
    randList.sort()
    time.stop()
    print(time.elapsedTime())
