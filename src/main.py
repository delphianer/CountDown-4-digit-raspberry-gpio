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
CountDownMan.setDisplayMaxDigits(ConfigMan.getInteger("display max digits"))

#debugging GPIO output start
for i in range(0,10):
    GPIOMan.display(i)
GPIOMan.display(100)
GPIOMan.display(1000)
GPIOMan.display(10000)
GPIOMan.display(100009)
GPIOMan.display(1000099)
GPIOMan.display(10000999)
GPIOMan.display(100009999)
GPIOMan.display(9999)
GPIOMan.display(999)
GPIOMan.display(99)
GPIOMan.display(9)
GPIOMan.display(0)
GPIOMan.display(0)
GPIOMan.display(0)
#debugging GPIO output end

# plan:
# 
# while (CountDownMan.ticksLeft()):
# 	GPIOMan.display(CountDownMan.getCurrentTickValue())
# 	CountDownMan.waitInterval()
