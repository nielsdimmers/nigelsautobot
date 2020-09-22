# This class handles the covid related commands
# At this moment, it's just '/covid'
# @author Niels Dimmers
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram
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
		covidDataYesterday = self.getCovidDataForDate(date.today() - timedelta(days=1))
		covidDataToday = self.getCovidDataForDate(date.today())
	
		# Message header content
		if covidDataYesterday != '':
			logging.info('Received infected %s yesterday ' % covidDataYesterday[1])
			responseMessage += self.const.INFECTED_MESSAGE_YESTERDAY % (covidDataYesterday[1], covidDataYesterday[2], covidDataYesterday[3])
		else:
						responseMessage += self.const.DATA_UNKNOWN % self.const.DATA_UNKNOWN_YESTERDAY
		if covidDataToday != '':
			logging.info('Received infected %s today ' % covidDataToday[1])
			responseMessage += self.const.INFECTED_MESSAGE % (covidDataToday[1], covidDataToday[2], covidDataToday[3])
		else:
			responseMessage += self.const.DATA_UNKNOWN % self.const.DATA_UNKNOWN_TODAY
		responseMessage += self.const.COVID_GRAPH_MESSAGE
		return responseMessage
		
	# Respond to the message with the covid data message
	def getCovidData(self, update, context):
		logging.info('Executing covid information command')
	
		# Send the response
		update.message.reply_text(self.generateCovidResponseMessage(), quote=False, parse_mode=telegram.ParseMode.MARKDOWN_V2)
		update.message.reply_photo(open('./'+self.const.GRAPH_FILENAME,'rb'), quote=False)
		update.message.reply_photo(open('./'+self.const.GRAPH_HOSIPITAL_FILENAME,'rb'), quote=False)
		update.message.reply_photo(open('./'+self.const.GRAPH_DECEASED_FILENAME,'rb'), quote=False)