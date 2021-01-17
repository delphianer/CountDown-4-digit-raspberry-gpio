import ConfigurationManager

ConfigMan = ConfigurationManager.ConfigurationManagerClass()

print("aimed date and time=",ConfigMan.getDateTime("aimed date and time"))

print("hello world")

# plan:
# GPIOMan = GPIOManager()
# CountDownMan = CountDownManager(ConfigMan.getDateTime("aimed date and time"))
# CountDownMan.setSmallestTickUnit(ConfigMan.getString("smallest tick intervall"))
# smallest tick unit: sec / min / hrs / days
# CountDownMan.setDisplayMaxDigits(ConfigMan.getInteger("display max digits"))
# while (CountDownMan.ticksLeft()):
# 	GPIOMan.display(CountDownMan.getCurrentTickValue())
# 	CountDownMan.waitIntervall()
