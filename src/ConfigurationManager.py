# ConfigurationManager handles everything about the Configuration

class ConfigurationManager:

	#todo: make private
	config = {"aimed date and time" : "todo:date and time",
		"smallest tick intervall" : "sec",
		"display max digits" : 4}

	def __init__(self):
		print("hello class world")

	def getDateTime(self, key):
		# todo: check if key exists...
		return self.config[key]
