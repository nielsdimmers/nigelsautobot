# Handles the temperature command from Telegram, can be executd directly to see the text message
# @author Niels Dimmers
import logging

from config import Config
from dbconnector import DBConnector
from const import Const


class TemperatureHandler:
	
	def __init__(self):
		self.config = Config()
		self.const = Const()
		logging.basicConfig(level=self.config.LOG_LEVEL, format=self.const.LOG_FORMAT)
	
	# Generate the response message
	def generateTempResponseMessage(self):
		dbconn = DBConnector()
		temperatureData = dbconn.getLatestTemperature()
		minTemperatureData = dbconn.getMinTemperature()
		maxTemperatureData = dbconn.getMaxTemperature()
		dateTime = temperatureData[0][0].strftime(self.const.TEMPERATURE_MESSAGE_DATE_FORMAT)
		returnMessage = ''
		
		if len(maxTemperatureData) > 0 and len(minTemperatureData) > 0:
			minTime = minTemperatureData[0][0].strftime(self.const.TEMPERATURE_MESSAGE_MINMAX_DATE_FORMAT)
			maxTime = maxTemperatureData[0][0].strftime(self.const.TEMPERATURE_MESSAGE_MINMAX_DATE_FORMAT)
			returnMessage = self.const.TEMPERATURE_MESSAGE % (dateTime, temperatureData[0][1], minTime, minTemperatureData[0][1], maxTime, maxTemperatureData[0][1])
		else:
			returnMessage = self.const.TEMPERATURE_MESSAGE_NOMINMAX % (dateTime, temperatureData[0][1])
		
		if temperatureData[0][2] is not None and len(temperatureData[0][2]) > 1:
			returnMessage += self.const.TEMPERATURE_MESSAGE_ALERT % temperatureData[0][2]
		
		returnMessage += self.const.TEMPERATURE_MESSAGE_CLOSURE
		
		return returnMessage
	
	# Get the response message and send it back to telegram
	def getTemperature(self, nigelsAutoBot):
		nigelsAutoBot.reply_text(nigelsAutoBot.escapeString(self.generateTempResponseMessage()))
		nigelsAutoBot.reply_photo('./'+self.const.TEMPERATURE_GRAPH_FILENAME)
		
if __name__ == '__main__':
	temperaturehandler = TemperatureHandler()
	print(temperaturehandler.generateTempResponseMessage())