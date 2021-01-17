import ConfigurationManager
import GPIOManager
import CountDownManager

ConfigMan = ConfigurationManager.ConfigurationManager()

GPIOMan = GPIOManager.GPIOManager()
CountDownMan = CountDownManager.CountDownManager(ConfigMan.getDateTime("aimed date and time"))
CountDownMan.setSmallestTickUnit(ConfigMan.getString("smallest tick intervall"))
CountDownMan.setDisplayMaxDigits(ConfigMan.getInteger("display max digits"))

while (CountDownMan.ticksLeft()):
    GPIOMan.display(CountDownMan.getCurrentTickValue())
    
print("countdown ended:", CountDownMan.getAimedDateTime())

cntDwn = 600 # 60 sec 404
while (cntDwn > 0):
    GPIOMan.display(404)