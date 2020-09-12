# This class contains all constant variables which are not configurable, like the json
# location, data names and output text templates. Note that allthough they are not part
# of configuration (config), they can be customised.
# @author Niels Dimmers
class Const:
	
	# Location of where the RIVM data is stored
	DATA_JSON_LOCATION = 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json'
	
	# Name of the date part of the data which is used in the system
	DATA_PUBLICATION_DATE = 'Date_of_publication'
	
	DATA_REPORTED_CASES = 'Total_reported'
	
	# the python date formatted date format as used in the data
	DATA_DATE_FORMAT = '%Y-%m-%d'
	
	# Snippet sent out when the amount of infected of today is not yet known
	DATA_UNKNOWN = 'nog niet bekend'
	
	# Message header, %s is the current date
	INFECTED_MESSAGE_HEADER = 'COVID-19 informatie voor %s:\n'
	
	# Python date format of the date in the message
	INFECTED_MESSAGE_DATE_FORMAT = '%A %-d %B %Y'
	
	# Total infected message
	INFECTED_MESSAGE = 'Het aantal nieuwe corona zieken gisteren gemeld was: %s, het aantal van vandaag is: %s'
	
	# The command to invoke the infected bod
	TELEGRAM_COMMAND_COVID = 'covid'
	
	TELEGRAM_COMMAND_VERSION = 'version'
	
	# The bot version (for in messages or something)
	BOT_VERSION = '0.6'
	
	# Message test for bot version
	BOT_VERSION_TEXT = 'Nigel\'s auto bot version %s'
	
	# date format of the graph (usually shorter)
	GRAPH_DATE_FORMAT = '%d-%m'
	
	# Constant name for production mode
	MODE_PRODUCTION = 'PROD'
	
	# Constant name for testing mode
	MODE_TEST = 'TEST'
	
	# Log format template
	LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
	
	# history graph filename
	GRAPH_FILENAME = 'data/historicGraph.png'
	
	DEMODATA_FILENAME = 'data/testdataAmersfoort.json'