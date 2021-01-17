import ConfigurationManager
import GPIOManager
import CountDownManager

ConfigMan = ConfigurationManager.ConfigurationManager()

# debugging output start
print("aimed date and time=",ConfigMan.getDateTime("aimed date and time"))
print("smallest tick intervall=",ConfigMan.getString("smallest tick intervall"))
print("display max digits=",ConfigMan.getInteger("display max digits"))
# debugging output end

GPIOMan = GPIOManager.GPIOManager()
CountDownMan = CountDownManager.CountDownManager(ConfigMan.getDateTime("aimed date and time"))
CountDownMan.setSmallestTickUnit(ConfigMan.getString("smallest tick intervall"))


# plan:
# CountDownMan.setDisplayMaxDigits(ConfigMan.getInteger("display max digits"))
# while (CountDownMan.ticksLeft()):
# 	GPIOMan.display(CountDownMan.getCurrentTickValue())
# 	CountDownMan.waitIntervall()
