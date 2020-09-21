# Generic modules to import
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import locale
import logging

# The below imports are all local
from config import Config
from const import Const
from covidhandler import CovidHandler
from temperaturehandler import TemperatureHandler

# Config and setup
const = Const()
config = Config()
locale.setlocale(locale.LC_TIME, config.LOCALE)

# Set logging level and info
logging.basicConfig(level=config.LOG_LEVEL,
                    format=const.LOG_FORMAT)

covidHandler = CovidHandler()

temperatureHandler = TemperatureHandler()

# generate version response, for testing purposes in separate function.
def generateVersionResponse():
	return const.BOT_VERSION_TEXT % const.BOT_VERSION

def getVersion(update, context):
	logging.info('Executing version information command')
	update.message.reply_text(generateVersionResponse(), quote=False)
	
def getInfo(update,context):
	logging.info('Executing information command')
	update.message.reply_text(const.BOT_INFO, quote=False)
	
# Set up the listener
def main():
	updater = Updater(config.BOT_KEY, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_COVID,covidHandler.getCovidData), True)
	dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_VERSION,getVersion), True)
	dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_TEMPERATURE,temperatureHandler.getTemperature), True)	
	dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_INFO,getInfo), True)	
	logging.info('Starting polling for commands')
	updater.start_polling()
	updater.idle()

if(config.RUN_MODE == const.MODE_TEST):
	print('Testing mode detected, just generate the response message and quit.')
	print(covidHandler.generateCovidResponseMessage())
	print('Also generating version response message:')
	print(generateVersionResponse())

	print('Goodbye.')
else:
	if __name__ == '__main__':
  	   main()