# This class contains information which should be configured by the user before starting
# the bot. Like the key and database connection information. Copy this file to config.py
# and modify as needed.
import logging
import sys

class Config:
	# The bot key
	BOT_KEY = '<TELEGRAM BOT KEY>'

	# MYSQL Database login
	DBUSER = '<DB NAME>'

	# MYSQL Database password
	DBPASSWD = '<DB PASSWORD>'

	# MYSQL Database IP
	DBHOST = '<DB IP>'

	# MYSQL Database name
	DBNAME = '<DB NAME>'
	
	# Locale to format (language) the date by. Make sure the locale is installed on the pc you're running the bot.
	LOCALE = 'nl_NL.UTF-8' # This setting has a default, but feel free to change it.
	
	# Number of days the graph should be long
	GRAPH_LENGTH = 21
	
	# Run the application in PRODuction or TEST mode
	RUN_MODE = 'TEST'
	
	# If the run mode is 'TEST', it's good to set this one to DEBUG so data is displayed on screen by default.
	# Good to have different on different environments
	LOG_LEVEL = logging.WARNING
	
	# Location of where the KNMI data is stored, this contains a key so is saved in the config file.
	DATA_KNMI_JSON_LOCATION = '<SOME KNMI DATA>'
	
	# Number of data points in the temperature graph
	TEMPERATURE_GRAPH_LIMIT = 10
		
	# If any commandline argument overrule the config, the global vars need to be overruled in the init
	def __init__(self):
		for command in sys.argv:
			if command == '--test':
				self.RUN_MODE = 'TEST'
				self.LOG_LEVEL = logging.DEBUG