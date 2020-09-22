# Log a single temperature record from the json data, create a graph to go with it.
import requests
import logging
import json
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

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

	# Use the database connection to retrieve the temperature information.
	def retrieveTemperatureData(self):
		temperatureData = requests.get(self.config.DATA_KNMI_JSON_LOCATION).json()
		db = DBConnector()
		alerttext = ''
		if temperatureData['liveweer'][0]['alarm'] == 1:
			alerttext = temperatureData['liveweer'][0]['alarmtxt']
		db.insertTemperatureLog(datetime.now(),temperatureData['liveweer'][0]['temp'],alerttext)
	
	# Create the graph to send the temperature information
	def createGraph(self):
		db = DBConnector()
		temperatureData = db.getTemperatureGraphData()
		x = [] # times
		y = [] # temps
		for i in range(len(temperatureData)-1,-1,-1):
			x.append(temperatureData[i][0].strftime(self.const.TEMPERATURE_GRAPH_DATE_FORMAT))
			y.append(temperatureData[i][1])
		
		figure(num=None, figsize=(16, 9), dpi=100, facecolor='w', edgecolor='k')
		plt.plot(x,y)
		plt.xlabel("Time")
		plt.ylabel("Temperature")
		plt.title('Temperature over time')

		logging.info('Save historic data graph for temperature')
		plt.savefig(self.const.TEMPERATURE_GRAPH_FILENAME)
			
	
if __name__ == '__main__':
	temperatureLogger = LogTemperature()
	temperatureLogger.retrieveTemperatureData()
	temperatureLogger.createGraph()