import logging

from config import Config
from dbconnector import DBConnector
from const import Const

from telegram.ext import Updater, InlineQueryHandler, CommandHandler

class TemperatureHandler:
	
	def __init__(self):
		self.config = Config()
		self.const = Const()
		logging.basicConfig(level=self.config.LOG_LEVEL, format=self.const.LOG_FORMAT)
	
	def generateTempResponseMessage(self):
		dbconn = DBConnector()
		temperature = dbconn.getLatestTemperature()
		return self.const.TEMPERATURE_MESSAGE % temperature
	
	def getTemperature(self, update, context):
		update.message.reply_text(self.generateTempResponseMessage(), quote=False)
		
if __name__ == '__main__':
	temperaturehandler = TemperatureHandler()
	print(temperaturehandler.generateTempResponseMessage())