# Generic modules to import
import locale
import logging

# The below imports are all local
from config import Config
from const import Const
from covidhandler import CovidHandler
from temperaturehandler import TemperatureHandler

class NigelsAutoBot:

	def __init__(self):
		# Config and setup
		self.const = Const()
		self.config = Config()
		locale.setlocale(locale.LC_TIME, self.config.LOCALE)
		# Set logging level and info
		logging.basicConfig(level=self.config.LOG_LEVEL,
												format=self.const.LOG_FORMAT)
		self.covidHandler = CovidHandler()
		self.temperatureHandler = TemperatureHandler()

	# generate version response, for testing purposes in separate function.
	def generateVersionResponse(self):
		return self.const.BOT_VERSION_TEXT % self.const.BOT_VERSION

	def escapeString(self, textMessage):
		return textMessage

	def reply_text(self, textMessage):	
		pass
		
	def reply_photo(self, photoLocation):
		pass

	def main(self):
		pass
