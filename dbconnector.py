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
	def updateDailyInfected(self,date, infected, hospitalised, deceased):
		query = 'SELECT * FROM dailyInfected WHERE date = \'%s\'' % date
		if self.getCount(query) == 0:
			query = 'INSERT INTO dailyInfected (date,infected,hospitalised,deceased) VALUES (\'%s\',%s,%s,%s)' % (date, infected, hospitalised, deceased)
		else:
			query = 'UPDATE dailyInfected SET infected = %s, hospitalised = %s, deceased = %s WHERE date =\'%s\'' % (infected, hospitalised, deceased, date)
		self.executeQuery(query)
		self.executeQuery('COMMIT')
	
	# Insert a new temperature log record
	# @param date the date for this temperature record
	# @param temperature the temperature for this record.
	def insertTemperatureLog(self,date,temperature,alerttext):
		query = 'INSERT INTO temperatureLog (date,temperature,alerttext) VALUES (\'%s\',%s,\'%s\')' % (date.strftime(self.const.SQL_DATE_FORMAT), temperature, alerttext) # self.const.DATA_DATE_FORMAT
		self.executeQuery(query)
		self.executeQuery('COMMIT')
	
	# Get the most recent temperature record for the textbased information
	# @result most recent temperature record together with the datetime it was logged.
	def getLatestTemperature(self):
		query = 'SELECT date,temperature,alerttext FROM temperatureLog WHERE date = (SELECT max(date) FROM temperatureLog)'
		temp = self.executeQuery(query, returnResult=True)
		return temp
	
	# Get today's maximum temperature
	# @result max temperature record with the datetime it was logged
	def getMaxTemperature(self):
		query = 'SELECT date,temperature FROM temperatureLog WHERE date >= CURDATE() AND temperature = (SELECT MAX(temperature) FROM temperatureLog WHERE date >= CURDATE())'
		return self.executeQuery(query, returnResult=True)
		
	# Get today's minimum temperature
	# @result min temperature record with the datetime it was logged
	def getMinTemperature(self):
		query = 'SELECT date,temperature FROM temperatureLog WHERE date >= CURDATE() AND temperature = (SELECT MIN(temperature) FROM temperatureLog WHERE date >= CURDATE())'
		return self.executeQuery(query, returnResult=True)
	
	# Get the most recent X temperature records for the graph information
	# @result an database connector result list with datetime-temperature values of the data
	def getTemperatureGraphData(self):
		query = 'SELECT date,temperature FROM temperatureLog ORDER BY date DESC LIMIT %s' % self.config.TEMPERATURE_GRAPH_LIMIT
		return self.executeQuery(query, returnResult=True)

	# Get the number of infected for the given date
	# @param date the date to get the number of infected for.
	def getDailyInfected(self,date):
		query = 'SELECT date,infected,hospitalised,deceased FROM dailyInfected WHERE date =\'%s\'' % date
		result = self.executeQuery(query, True)
		if len(result) > 0:
			return result[0]
		else:
			return ''
	
	# Close the database connection
	def __del__(self):
		self.database.close()