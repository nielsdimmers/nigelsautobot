# This class contains all constant variables which are not configurable, like the json
# location, data names and output text templates. Note that allthough they are not part
# of configuration (config), they can be customised.
# @author Niels Dimmers
class Const:
	
	# Location of where the RIVM data is stored
	DATA_JSON_LOCATION = 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json'
	
	# Name of the date part of the data which is used in the system
	DATA_PUBLICATION_DATE = 'Date_of_publication'
	
	# The data field values
	DATA_REPORTED_CASES = 'Total_reported'
	
	DATA_DECEASED = 'Deceased'
	
	DATA_HOSPITALISED = 'Hospital_admission'
	
	# the python date formatted date format as used in the data
	DATA_DATE_FORMAT = '%Y-%m-%d'
	
	SQL_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
	
	# Snippet sent out when the amount of infected of today is not yet known
	DATA_UNKNOWN = 'nog niet bekend'
	
	# Message header, %s is the current date
	INFECTED_MESSAGE_HEADER = '*COVID\-19 informatie voor %s:*\n'
	
	# Python date format of the date in the message
	INFECTED_MESSAGE_DATE_FORMAT = '%A %-d %B %Y'
	
	# Total infected message
	INFECTED_MESSAGE = 'Het aantal corona besmettingen van vandaag is: %s, er zijn %s mensen in het ziekenhuis opgenomen en %s mensen aan corona overleden.'
	
	INFECTED_MESSAGE_YESTERDAY = 'Gisteren waren er %s besmettingen, zijn er %s mensen in het ziekenhuis opgenomen en %s mensen aan corona overleden.\n'
	
	TEMPERATURE_MESSAGE = 'Het laatste meetmoment is %s en toen was de temperatuur in Amersfoort: %s°C. Het koudste moment tot nu toe vandaag was om %s en toen was het %s°C, het warmste moment was om %s en toen was het %s°C.'
	
	TEMPERATURE_MESSAGE_NOMINMAX = 'Het laatste meetmoment is %s en toen was de temperatuur in Amersfoort: %s°C.'
	
	TEMPERATURE_MESSAGE_ALERT = '\nOp dit tijdstip geldt een weer alarm:\n%s'
	
	TEMPERATURE_MESSAGE_CLOSURE = '\nHierna volgt een grafiek met de temperatuur over de afgelopen tijd.'
	
	# The command to invoke the infected bod
	TELEGRAM_COMMAND_COVID = 'covid'
	
	TELEGRAM_COMMAND_VERSION = 'version'
	
	TELEGRAM_COMMAND_TEMPERATURE = 'temp'
	
	TELEGRAM_COMMAND_INFO = 'help'
	
	# The bot version (for in messages or something)
	BOT_VERSION = '0.9'
	
	# Message test for bot version
	BOT_VERSION_TEXT = 'Nigel\'s auto bot version %s'
	
	# date format of the graph (usually shorter)
	GRAPH_DATE_FORMAT = '%d-%m'
	
	GRAPH_TITLE_DATE_FORMAT = '%Y-%m-%d'
	
	# Constant name for production mode
	MODE_PRODUCTION = 'PROD'
	
	# Constant name for testing mode
	MODE_TEST = 'TEST'
	
	# Log format template
	LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
	
	# history graph filename
	GRAPH_FILENAME = 'data/historicInfectionsGraph.png'
	
	GRAPH_HOSIPITAL_FILENAME = 'data/hospitalisationGraph.png'
	
	GRAPH_DECEASED_FILENAME = 'data/deceasedGraph.png'
	
	# temperature graph filename
	TEMPERATURE_GRAPH_FILENAME = 'data/temperatureGraph.png'
	
	TEMPERATURE_GRAPH_DATE_FORMAT = '%H:%M'
	
	TEMPERATURE_MESSAGE_DATE_FORMAT = '%A %-d %B %Y %H:%M'
	
	TEMPERATURE_MESSAGE_MINMAX_DATE_FORMAT = '%H:%M'
	
	# Filename location of the demo data
	DEMODATA_FILENAME = 'data/testdataAmersfoort.json'
	
	BOT_INFO = 'These are the commands you can use for this bot:\n/help - display this help information\n/version - display version information\n/covid - display covid information\n/temp - display temperature information'