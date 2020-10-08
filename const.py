# This class contains all constant variables which are not configurable, like the json
# location, data names and output text templates. Note that allthough they are not part
# of configuration (config), they can be customised.
# @author Niels Dimmers
class Const:
	
	# Location of where the RIVM data is stored
	DATA_JSON_LOCATION = 'https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json'
	
	# The data field values
	DATA_PUBLICATION_DATE = 'Date_of_publication'
	DATA_REPORTED_CASES = 'Total_reported'
	DATA_DECEASED = 'Deceased'
	DATA_HOSPITALISED = 'Hospital_admission'
	
	# the python date formatted date format as used in the data
	DATA_DATE_FORMAT = '%Y-%m-%d'
	
	# the python date formatted date format as used in SQL, including time
	SQL_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
	
	# Snippet sent out when the amount of infected of today is not yet known
	DATA_UNKNOWN = 'Het aantal besmettingen van %s is niet bekend\.'
	DATA_UNKNOWN_YESTERDAY = 'gisteren'
	DATA_UNKNOWN_TODAY = 'vandaag'
		
	# Text for the infected message
	INFECTED_MESSAGE_HEADER = '*COVID\-19 informatie voor %s:*\n'
	INFECTED_MESSAGE_DATE_FORMAT = '%A %-d %B %Y'
	INFECTED_MESSAGE = 'Het aantal corona besmettingen van vandaag is: %s, er zijn %s mensen in het ziekenhuis opgenomen en %s mensen aan corona overleden\.'
	INFECTED_MESSAGE_YESTERDAY = 'Gisteren waren er %s besmettingen, zijn er %s mensen in het ziekenhuis opgenomen en %s mensen aan corona overleden\.\n'
	COVID_GRAPH_MESSAGE = ' Hierna volgen grafieken van de recente besmettingen, ziekenhuis opnamen en overlijdens ten gevolge van COVID\-19\.'
	
	# Text for the temperature message
	TEMPERATURE_MESSAGE = 'Het laatste meetmoment is %s en toen was de temperatuur in Amersfoort: %s°C. Het koudste moment tot nu toe vandaag was om %s en toen was het %s°C, het warmste moment was om %s en toen was het %s°C.'
	TEMPERATURE_MESSAGE_NOMINMAX = 'Het laatste meetmoment is %s en toen was de temperatuur in Amersfoort: %s°C.'	
	TEMPERATURE_MESSAGE_ALERT = '\nOp dit tijdstip geldt een weer alarm:\n%s'
	TEMPERATURE_MESSAGE_CLOSURE = '\nHierna volgt een grafiek met de temperatuur over de afgelopen tijd.'
	TEMPERATURE_MESSAGE_DATE_FORMAT = '%A %-d %B %Y %H:%M'
	TEMPERATURE_MESSAGE_MINMAX_DATE_FORMAT = '%H:%M'
	
	# Telegram commands
	TELEGRAM_COMMAND_COVID = 'covid'
	TELEGRAM_COMMAND_VERSION = 'version'
	TELEGRAM_COMMAND_TEMPERATURE = 'temp'
	TELEGRAM_COMMAND_INFO = 'help'
	TELEGRAM_COMMAND_PREFIX = '/'
	
	# The bot version (for in messages or something)
	BOT_VERSION = '0.12'
	
	# Message test for bot version
	BOT_VERSION_TEXT = 'Nigel\'s auto bot version %s'
	
	# date format of the graph (usually shorter)
	GRAPH_DATE_FORMAT = '%d-%m'
	
	# date format of the title of the graph
	GRAPH_TITLE_DATE_FORMAT = '%Y-%m-%d'
	
	# Constant name for production mode
	MODE_PRODUCTION = 'PROD'
	
	# Constant name for testing mode
	MODE_TEST = 'TEST'
	
	# Log format template
	LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
	
	# Graph filenames for covid information
	GRAPH_FILENAME = 'data/historicInfectionsGraph.png'
	GRAPH_HOSIPITAL_FILENAME = 'data/hospitalisationGraph.png'
	GRAPH_DECEASED_FILENAME = 'data/deceasedGraph.png'
	
	# temperature graph filename
	TEMPERATURE_GRAPH_FILENAME = 'data/temperatureGraph.png'
	
	TEMPERATURE_GRAPH_DATE_FORMAT = '%H:%M'
	
	# Filename location of the demo data
	DEMODATA_FILENAME = 'data/testdataAmersfoort.json'
	
	# Bot information message (which commands are available?)
	BOT_INFO = 'These are the commands you can use for this bot:\n/help - display this help information\n/version - display version information\n/covid - display covid information\n/temp - display temperature information'