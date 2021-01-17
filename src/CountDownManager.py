# CountDownManager implements all datetime functions and everything necessary for counting down towards a datetime
from datetime import datetime

class CountDownManager:
    
    __aimedDatetime = datetime.now()
    __smallestTickUnit = 'sec'
    __displayMaxDigits = 4

    def __init__(self, aimedDateTime):
        self.__aimedDatetime = aimedDateTime

    def setSmallestTickUnit(self, smallestTickUnit):
        self.__smallestTickUnit = smallestTickUnit

    def setDisplayMaxDigits(self, displayMaxDigits):
        self.__displayMaxDigits = displayMaxDigits

    # todo: handle smallest tick unit: sec / min / hrs / days