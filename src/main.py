import ConfigurationManager
import GPIOManager

ConfigMan = ConfigurationManager.ConfigurationManager()

print("aimed date and time=",ConfigMan.getDateTime("aimed date and time"))
print("smallest tick intervall=",ConfigMan.getDateTime("smallest tick intervall"))
print("display max digits=",ConfigMan.getDateTime("display max digits"))

GPIOMan = GPIOManager.GPIOManager()

# plan:

# CountDownMan = CountDownManager(ConfigMan.getDateTime("aimed date and time"))
# CountDownMan.setSmallestTickUnit(ConfigMan.getString("smallest tick intervall"))
# smallest tick unit: sec / min / hrs / days
# CountDownMan.setDisplayMaxDigits(ConfigMan.getInteger("display max digits"))
# while (CountDownMan.ticksLeft()):
# 	GPIOMan.display(CountDownMan.getCurrentTickValue())
# 	CountDownMan.waitIntervall()
