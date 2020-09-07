from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from datetime import date
from datetime import timedelta
import mysql.connector
import config

covidArray = {}
covidData = requests.get('https://data.rivm.nl/covid-19/COVID-19_aantallen_gemeente_per_dag.json').json()
for rivmData in covidData:
	if rivmData['Date_of_publication'] in covidArray:
		covidArray[rivmData['Date_of_publication']] += int(rivmData['Total_reported'])
	else:
		covidArray[rivmData['Date_of_publication']] = int(rivmData['Total_reported'])


database = mysql.connector.connect(host=config.DBHOST,database=config.DBNAME,user=config.DBUSER,password=config.DBPASSWD)
cursor = database.cursor()

for date in covidArray:
	try:
		query = 'SELECT * FROM dailyInfected WHERE date = \''+date+ '\''
		cursor.execute(query)
		cursor.fetchall()
		if cursor.rowcount == 0:
			query = 'INSERT INTO dailyInfected (date,infected) VALUES (\''+str(date)+'\','+str(covidArray[date])+')'
			print(query)
			cursor.execute(query)
		else:
			query = 'UPDATE dailyInfected SET infected = '+str(covidArray[date])+' WHERE date =\''+date+'\''
			print(query)
			cursor.execute(query)
		cursor.execute('COMMIT')
	except mysql.connector.Error as err:
		print(err.msg)
#	else: