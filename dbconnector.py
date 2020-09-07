# This is the only file which should contain SQL queries at the moment (aside from the 
# create tables script), which makes this module responsible for the connection to the 
# database. Connection details are specified in the config module. This makes it easier to
# switch to a different database type.
# @author Niels Dimmers
import mysql.connector
from config import Config
from const import Const

class DBConnector:
	# setup database connection
	
	def __init__(self):
		self.config = Config()
		self.database = mysql.connector.connect(host=self.config.DBHOST,database=self.config.DBNAME,user=self.config.DBUSER,password=self.config.DBPASSWD)
		self.cursor = self.database.cursor()
		self.const = Const()

	# executes the database query given in the param, and prints any errors resulting from it.
	def executeQuery(self, query, returnResult = False):
		try:
			self.cursor.execute(query)
			if returnResult:
				return self.cursor.fetchall()
		except mysql.connector.Error as err:
			print(err.msg)

	def getCount(self, selectQuery):
		result = self.executeQuery(selectQuery, True)
		return len(result)

	def updateDailyInfected(self,date, infected):
		query = 'SELECT * FROM dailyInfected WHERE date = \'%s\'' % date
		if self.getCount(query) == 0:
			query = 'INSERT INTO dailyInfected (date,infected) VALUES (\'%s\',%s)' % (date, infected)
		else:
			query = 'UPDATE dailyInfected SET infected = %s WHERE date =\'%s\'' % (infected, date)
		self.executeQuery(query)
		self.executeQuery('COMMIT')

		
	def getDailyInfected(self,date):
		query = 'SELECT date,infected FROM dailyInfected WHERE date =\'%s\'' % date
		result = self.executeQuery(query, True)
		if len(result) > 0:
			return result[0][1]
		else:
			return self.const.DATA_UNKNOWN
		
	def __del__(self):
		self.database.close()