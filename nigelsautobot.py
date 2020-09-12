# Generic modules to import
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from datetime import date
from datetime import timedelta
import locale
import logging

# The below imports are all local
from config import Config
from dbconnector import DBConnector
from const import Const

# Config and setup
const = Const()
config = Config()
locale.setlocale(locale.LC_TIME, config.LOCALE)

# Set logging level and info
logging.basicConfig(level=config.LOG_LEVEL,
                    format='%(asctime)s - %(levelname)s - %(message)s')
                    
# Get the covid data for the given date
# @param compareDate the datetime record to get the covid data for
def getCovidDataForDate(compareDate):
	dateStr = compareDate.strftime(const.DATA_DATE_FORMAT)
	dbconn = DBConnector()
	return dbconn.getDailyInfected(dateStr)

def getVersion(update, context):
	logging.info('Executing version information command')
	update.message.reply_text(const.BOT_VERSION_TEXT % const.BOT_VERSION)

# Respond to the message with the covid data message
def getCovidData(update, context):
	logging.info('Executing covid information command')
	# Message header with date
	responseMessage = const.INFECTED_MESSAGE_HEADER % date.today().strftime(const.INFECTED_MESSAGE_DATE_FORMAT)
	
	# Calculate the infected
	infectedYesterday = str(getCovidDataForDate(date.today() - timedelta(days=1)))
	infectedToday = str(getCovidDataForDate(date.today()))
	
	logging.info('Received infected %s today and %s yesterday' % (infectedToday, infectedYesterday))
	# Message header content
	responseMessage += const.INFECTED_MESSAGE % (infectedYesterday, infectedToday)
	
	# Send the response
	update.message.reply_text(responseMessage)
	update.message.reply_photo(open('./historicGraph.png','rb'))

# Set up the listener
def main():
    updater = Updater(config.BOT_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_COVID,getCovidData), True)
    dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND_VERSION,getVersion), True)
    logging.info('Starting polling for commands')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
     main()