from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from datetime import date
from datetime import timedelta
import mysql.connector
import config

covidData = ""

covidArray = {}

database = mysql.connector.connect(host=config.DBHOST,database=config.DBNAME,user=config.DBUSER,password=config.DBPASSWD)
cursor = database.cursor()

# Looks a bit ugly, but gets the info from the database and returns it.
def getCovidDataForDate(compareDate):
	dateStr = compareDate.strftime('%Y-%m-%d')
	query = 'SELECT date,infected FROM dailyInfected WHERE date =\''+dateStr+'\''
	cursor.execute(query)
	result = cursor.fetchall()
	if cursor.rowcount > 0:
		return result[0][1]
	else:
		return 'nog niet bekend'

def getCovidData(bot, update):
  responseMessage = 'COVID-19 informatie voor '+date.today().strftime('%d-%m-%Y')+' voor Nederland:\n'
  responseMessage += 'Het aantal nieuwe corona zieken gisteren gemeld was: ' + str(getCovidDataForDate(date.today() - timedelta(days=1)))
  responseMessage += ', het aantal van vandaag is: '+str(getCovidDataForDate(date.today()))+'.'
  chat_id = update.message.chat_id
  bot.send_message(chat_id=chat_id, text=responseMessage)

def main():
    updater = Updater(config.BOT_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('covid',getCovidData), True)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
     main()