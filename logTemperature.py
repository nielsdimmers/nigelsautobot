# Log a single temperature record from the json data
import requests
import logging
import json
from datetime import datetime

from dbconnector import DBConnector
from const import Const
from config import Config




class LogTemperature:

	def __init__(self):
		self.config = Config()
		# setup variables
		self.const = Const();
		# Set logging level and info
		logging.basicConfig(level=self.config.LOG_LEVEL, format=self.const.LOG_FORMAT)

	def retrieveTemperatureData(self):
		temperatureData = requests.get(self.config.DATA_KNMI_JSON_LOCATION).json()
		db = DBConnector()
		db.insertTemperatureLog(datetime.now(),temperatureData['liveweer'][0]['temp'])
	
if __name__ == '__main__':
	temperatureLogger = LogTemperature()
	temperatureLogger.retrieveTemperatureData()