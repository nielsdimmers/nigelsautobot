# This class handles the covid related commands
# At this moment, it's just '/covid'
# @author Niels Dimmers
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from datetime import date
from datetime import timedelta
import locale
import logging

from config import Config
from dbconnector import DBConnector
from const import Const

class CovidHandler:
	
	# Initialise this handler
	def __init__(self):
		self.config = Config()
		self.const = Const()
		logging.basicConfig(level=self.config.LOG_LEVEL, format=self.const.LOG_FORMAT)
		
	# Get the covid data for the given date
	# @param compareDate the datetime record to get the covid data for
	def getCovidDataForDate(self,compareDate):
		dateStr = compareDate.strftime(self.const.DATA_DATE_FORMAT)
		dbconn = DBConnector()
		return dbconn.getDailyInfected(dateStr)
		
	# Generates the covid response message
	# @return a string with the response message
	def generateCovidResponseMessage(self):
		# Message header with date
		responseMessage = self.const.INFECTED_MESSAGE_HEADER % date.today().strftime(self.const.INFECTED_MESSAGE_DATE_FORMAT)
	
		# Calculate the infected
		infectedYesterday = str(self.getCovidDataForDate(date.today() - timedelta(days=1)))
		infectedToday = str(self.getCovidDataForDate(date.today()))
	
		logging.info('Received infected %s today and %s yesterday' % (infectedToday, infectedYesterday))
		# Message header content
		responseMessage += self.const.INFECTED_MESSAGE % (infectedYesterday, infectedToday)
	
		return responseMessage
		
	# Respond to the message with the covid data message
	def getCovidData(self, update, context):
		logging.info('Executing covid information command')
	
		# Send the response
		update.message.reply_text(self.generateCovidResponseMessage(), quote=False)
		update.message.reply_photo(open('./'+const.GRAPH_FILENAME,'rb'), quote=False)