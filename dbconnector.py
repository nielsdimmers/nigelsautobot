# This is the only file which should contain SQL queries at the moment (aside from the 
# create tables script), which makes this module responsible for the connection to the 
# database. Connection details are specified in the config module. This makes it easier to
# switch to a different database type.
# @author Niels Dimmers
import mysql.connector
import logging
from config import Config
from const import Const

class DBConnector:
	# setup database connection
	
	# Initialize the connector, set up the database connection
	def __init__(self):
		self.config = Config()
		# Set logging level and info
		logging.basicConfig(level=self.config.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.database = mysql.connector.connect(host=self.config.DBHOST,database=self.config.DBNAME,user=self.config.DBUSER,password=self.config.DBPASSWD)
		self.cursor = self.database.cursor()
		self.const = Const()

	# executes the database query given in the param, and prints any errors resulting from it.
	# All this is encapsulated inside an try-except block.
	# @param query the SQL query to run (can be anything)
	# @param returnResult set to True if you want a result back
	def executeQuery(self, query, returnResult = False):
		try:
			logging.debug('execute database query %s' % query)
			self.cursor.execute(query)
			if returnResult:
				return self.cursor.fetchall()
		except mysql.connector.Error as err:
			print(err.msg)
	
	# Executes your query (using executeQuery) and return the length of the result.
	# @param selectQuery the query you want to count
	# @result the number of records returned. If the query is OK, result is always an int >= 0
	def getCount(self, selectQuery):
		result = self.executeQuery(selectQuery, True)
		return len(result)

	# Set the datbase record of date to infected value. Any previous value is removed, if
	# a value does not exist it is inserted.
	# @param date the date to insert or update (unique key)
	# @param infected the infected count to set it to.
	def updateDailyInfected(self,date, infected):
		query = 'SELECT * FROM dailyInfected WHERE date = \'%s\'' % date
		if self.getCount(query) == 0:
			query = 'INSERT INTO dailyInfected (date,infected) VALUES (\'%s\',%s)' % (date, infected)
		else:
			query = 'UPDATE dailyInfected SET infected = %s WHERE date =\'%s\'' % (infected, date)
		self.executeQuery(query)
		self.executeQuery('COMMIT')
	
	def insertTemperatureLog(self,date,temperature):
		query = 'INSERT INTO temperatureLog (date,temperature) VALUES (\'%s\',%s)' % (date.strftime(self.const.SQL_DATE_FORMAT), temperature) # self.const.DATA_DATE_FORMAT
		self.executeQuery(query)
		self.executeQuery('COMMIT')
		
	def getLatestTemperature(self):
		query = 'SELECT temperature FROM temperatureLog WHERE date = (SELECT max(date) FROM temperatureLog)'
		temp = self.executeQuery(query, returnResult=True)
		return temp[0][0]

	# Get the number of infected for the given date
	# @param date the date to get the number of infected for.
	def getDailyInfected(self,date):
		query = 'SELECT date,infected FROM dailyInfected WHERE date =\'%s\'' % date
		result = self.executeQuery(query, True)
		if len(result) > 0:
			return result[0][1]
		else:
			return self.const.DATA_UNKNOWN
	
	# Close the database connection
	def __del__(self):
		self.database.close()