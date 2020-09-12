# This class contains information which should be configured by the user before starting
# the bot. Like the key and database connection information. Copy this file to config.py
# and modify as needed.
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
	
	# Good to have different on different environments
	LOG_LEVEL = logging.INFO
	
	# Number of days the graph should be long
	GRAPH_LENGTH = 21