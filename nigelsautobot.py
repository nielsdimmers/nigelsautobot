from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from datetime import date
from datetime import timedelta

covidData = ""

covidArray = {}

def refreshCovidData():
	global covidData
	global covidArray
	covidArray = {}
	covidData = requests.get('https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json').json()
	for rivmData in covidData:
		dataDateArray = rivmData['Date_of_publication'].split('-');
		dataDate =  date(int(dataDateArray[0]),int(dataDateArray[1]),int(dataDateArray[2]))
		if rivmData['Date_of_publication'] in covidArray:
			covidArray[rivmData['Date_of_publication']] += int(rivmData['Total_reported'])
		else:
			covidArray[rivmData['Date_of_publication']] = int(rivmData['Total_reported'])
		#covidArray[rivmData['Date_of_publication']] += int(rivmData['Total_reported'])

def getCovidDataForDate(compareDate):
	dateStr = compareDate.strftime('%Y-%m-%d')
	if dateStr in covidArray:
		return covidArray[dateStr]
	else:
		return 'unknown'

def getCovidData(bot, update):
    refreshCovidData()
    responseMessage = 'COVID-19 informatie voor '+date.today().strftime('%d-%m-%Y')+' voor Nederland:\n'
    responseMessage += 'Het aantal nieuwe corona zieken gisteren gemeld was: ' + str(getCovidDataForDate(date.today() - timedelta(days=1)))
    responseMessage += ', het aantal van vandaag is: '+str(getCovidDataForDate(date.today()))+'.'
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=responseMessage)

def main():
    updater = Updater('<Put your key here...>')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('covid',getCovidData))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()