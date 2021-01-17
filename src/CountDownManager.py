# CountDownManager implements all datetime functions and everything necessary for counting down towards a datetime
from datetime import datetime

class CountDownManager:
    
    __aimedDatetime = datetime.now()

    def __init__(self, aimedDateTime):
        self.__aimedDatetime = aimedDateTime