# Refreshes the covid data in the database, in general, all data is updated / refreshed
# new records are inserted, existing records are updated
# @author Niels Dimmers
import requests
import logging
from dbconnector import DBConnector
from const import Const
from config import Config

config = Config()

# Set logging level and info
logging.basicConfig(level=config.LOG_LEVEL,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# setup variables
const = Const();
covidArray = {}

# Retrieve the covid data from the remote location. It's arount 6Mb so it takes some time
logging.info('Retrieving the json from the RIVM website, this usually takes a bit of time.')
covidData = requests.get(const.DATA_JSON_LOCATION).json()

# Loop over the data and add where needed, otherwise create the entire table. This has the
# disadvantage that the entire dataset is in memory (twice) but the advantage that it greatly
# reduces SQL communication compared to saving it directly to SQL.
logging.info('Calculating results')
for rivmData in covidData:
	if rivmData[const.DATA_PUBLICATION_DATE] in covidArray:
		covidArray[rivmData[const.DATA_PUBLICATION_DATE]] += int(rivmData[const.DATA_REPORTED_CASES])
	else:
		covidArray[rivmData[const.DATA_PUBLICATION_DATE]] = int(rivmData[const.DATA_REPORTED_CASES])

logging.info('Start the DB connector and add the results to the database')
# start the database connector
db = DBConnector()

# Push it all to database.
for date in covidArray:
	db.updateDailyInfected(date,covidArray[date])