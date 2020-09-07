# Generic modules to import
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from datetime import date
from datetime import timedelta
import locale

# The below imports are all local
from config import Config
from dbconnector import DBConnector
from const import Const

# Config and setup
const = Const()
config = Config()
locale.setlocale(locale.LC_TIME, const.LOCALE)


def getCovidDataForDate(compareDate):
	dateStr = compareDate.strftime(const.DATA_DATE_FORMAT)
	dbconn = DBConnector()
	return dbconn.getDailyInfected(dateStr)
	
def getCovidData(bot, update):
  responseMessage = const.INFECTED_MESSAGE_HEADER % date.today().strftime(const.INFECTED_MESSAGE_DATE_FORMAT)
  infectedYesterday = str(getCovidDataForDate(date.today() - timedelta(days=1)))
  infectedToday = str(getCovidDataForDate(date.today()))
  responseMessage += const.INFECTED_MESSAGE % (infectedYesterday, infectedToday)
  chat_id = update.message.chat_id
  bot.send_message(chat_id=chat_id, text=responseMessage)

def main():
    updater = Updater(config.BOT_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler(const.TELEGRAM_COMMAND,getCovidData), True)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
     main()