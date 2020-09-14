# Refreshes the covid data in the database, in general, all data is updated / refreshed
# new records are inserted, existing records are updated
# @author Niels Dimmers	
import requests
import logging
import json
from datetime import date
from datetime import timedelta
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

from dbconnector import DBConnector
from const import Const
from config import Config

class CovidDataRefresher:

	def __init__(self):
		self.config = Config()
		# setup variables
		self.const = Const();
		# Set logging level and info
		logging.basicConfig(level=self.config.LOG_LEVEL, format=self.const.LOG_FORMAT)
		
	def retrieveData(self, runMode = 'UNKNOWN'):
		if runMode == 'UNKNOWN':
			runMode = self.config.RUN_MODE
		if (runMode  == self.const.MODE_TEST):
			# load testing data so it's consistent (yes, this is actually put in the database.)
			with open(self.const.DEMODATA_FILENAME) as json_file:
				covidData = json.load(json_file)
		else:
			# Retrieve the covid data from the remote location. It's arount 29Mb so it takes some time
			logging.info('Retrieving the json from the RIVM website, this usually takes a bit of time.')
			covidData = requests.get(self.const.DATA_JSON_LOCATION).json()
		return covidData

	# Loop over the data and add where needed, otherwise create the entire table. This has the
	# disadvantage that the entire dataset is in memory (twice) but the advantage that it greatly
	# reduces SQL communication compared to saving it directly to SQL.		
	def addByDay(self, covidData):
		logging.info('Calculating results')
		covidArray = {}
		for rivmData in covidData:
			if rivmData[self.const.DATA_PUBLICATION_DATE] in covidArray:
				covidArray[rivmData[self.const.DATA_PUBLICATION_DATE]] += int(rivmData[self.const.DATA_REPORTED_CASES])
			else:
				covidArray[rivmData[self.const.DATA_PUBLICATION_DATE]] = int(rivmData[self.const.DATA_REPORTED_CASES])
		return covidArray
	
	def fillDB(self, covidArray):
		logging.info('Start the DB connector and add the results to the database')
		# start the database connector
		db = DBConnector()

		# Push it all to database.
		for infectionDate in covidArray:
			db.updateDailyInfected(infectionDate,covidArray[infectionDate])

	def createGraph(self,covidArray):
		# Since all the data is here, let's try to make a graph.
		x = [] # dates
		y = [] # infections

		anchorDate = date.today()

		if self.config.RUN_MODE == self.const.MODE_TEST:
			# In testing mode, there's data at least until Sept 10th, so we want the graph to be for that period
			anchorDate = date(year=2020,month=9,day=10)

		logging.info('Gathering info for the graph')
		for i in range(self.config.GRAPH_LENGTH,-1,-1):
			graphDate = anchorDate - timedelta(days=i)
			if graphDate.strftime(self.const.DATA_DATE_FORMAT) in covidArray:
				x.append(graphDate.strftime(self.const.GRAPH_DATE_FORMAT))
				y.append(covidArray[graphDate.strftime(self.const.DATA_DATE_FORMAT)])

		figure(num=None, figsize=(16, 9), dpi=100, facecolor='w', edgecolor='k')
		plt.plot(x,y)
		plt.xlabel("infections")
		plt.ylabel("data")
		plt.title('infected per day')

		logging.info('Save historic data graph')
		plt.savefig(self.const.GRAPH_FILENAME)

	def updateCovidData(self):
		covidData = self.retrieveData()
		covidArray = self.addByDay(covidData)
		self.fillDB(covidArray)
		self.createGraph(covidArray)
		
if __name__ == '__main__':
	refresher = CovidDataRefresher()
	refresher.updateCovidData()