# ConfigurationManager handles everything about the Configuration
from datetime import datetime

class ConfigurationManager:

	__config = {
		"aimed date and time" : "2021-04-04T00:00:00", # easter sunday, using utc time
		"smallest tick intervall" : "sec", # smallest tick unit: sec / min / hrs / days
		"display max digits" : 4
		}
	datetimeFormat = '%Y-%m-%dT%H:%M:%S'
	defaultValueIfNoKey = "No Value Found For Key"

	def __init__(self):
		pass

	def getAny(self, key):
		if key in self.__config:
			return self.__config[key]
		else:
			return self.defaultValueIfNoKey

	def getDateTime(self, key):
		# todo: default?
		return datetime.strptime(self.getAny(key), self.datetimeFormat)

	def getInteger(self, key):
		# todo: default?
		return int(self.getAny(key))

	def getString(self, key):
		# todo: default?
		return self.getAny(key)