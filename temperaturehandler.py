# Handles the temperature command from Telegram, can be executd directly to see the text message
# @authoer Niels Dimmers
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
	
	# Generate the response message
	def generateTempResponseMessage(self):
		dbconn = DBConnector()
		temperatureData = dbconn.getLatestTemperature()
		dateTime = temperatureData[0][0].strftime(self.const.TEMPERATURE_MESSAGE_DATE_FORMAT)
		return self.const.TEMPERATURE_MESSAGE % (dateTime, temperatureData[0][1])
	
	# Get the response message and send it back to telegram
	def getTemperature(self, update, context):
		update.message.reply_text(self.generateTempResponseMessage(), quote=False)
		update.message.reply_photo(open('./'+self.const.TEMPERATURE_GRAPH_FILENAME,'rb'), quote=False)
		
if __name__ == '__main__':
	temperaturehandler = TemperatureHandler()
	print(temperaturehandler.generateTempResponseMessage())