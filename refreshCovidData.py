import requests
from datetime import date
from dbconnector import DBConnector
from const import Const

const = Const();

covidArray = {}
covidData = requests.get(const.DATA_JSON_LOCATION).json()
for rivmData in covidData:
	if rivmData[const.DATA_PUBLICATION_DATE] in covidArray:
		covidArray[rivmData[const.DATA_PUBLICATION_DATE]] += int(rivmData[const.DATA_REPORTED_CASES])
	else:
		covidArray[rivmData[const.DATA_PUBLICATION_DATE]] = int(rivmData[const.DATA_REPORTED_CASES])

db = DBConnector()

for date in covidArray:
	db.updateDailyInfected(date,covidArray[date])