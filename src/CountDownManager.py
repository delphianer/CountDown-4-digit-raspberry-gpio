# CountDownManager implements all datetime functions and everything necessary for counting down towards a datetime
from datetime import datetime

class CountDownManager:
    
    __aimedDatetime = datetime.now()
    __smallestTickUnit = 'sec'
    __maxNumberOnDisplay = 9999

    def __init__(self, aimedDateTime):
        self.__aimedDatetime = aimedDateTime

    def setSmallestTickUnit(self, smallestTickUnit):
        self.__smallestTickUnit = smallestTickUnit

    def setDisplayMaxDigits(self, displayMaxDigits):
        self.__maxNumberOnDisplay = 10 ** displayMaxDigits - 1

    def ticksLeft(self):
        return self.__aimedDatetime > datetime.now()

    def getCurrentTickValue(self):
        timeleft = self.__aimedDatetime - datetime.now()
        secondsLeft = timeleft.days * 24 * 60 * 60 + timeleft.seconds
        minutesLeft = secondsLeft // 60
        hoursLeft = minutesLeft // 60
        daysLeft = hoursLeft // 24
        
        if self.__maxNumberOnDisplay < secondsLeft:
            ticksLeft = secondsLeft
        elif self.__maxNumberOnDisplay < minutesLeft:
            ticksLeft = secondsLeft
        elif self.__maxNumberOnDisplay < hoursLeft:
            ticksLeft = secondsLeft
        else:
            ticksLeft = daysLeft
        return ticksLeft
    
    def getAimedDateTime(self):
        return datetime.strftime(self.__aimedDatetime, "%Y-%m-%d %H:%M:%S")

    # todo: handle smallest tick unit: sec / min / hrs / days