# This script is meant to be executed once to create the tables in the database.
# It creates the table, at this moment, no data is persistent so this script can easily be
# re-run without any issues, just run refreshCovidData.py after it.
# @author Niels Dimmers
import mysql.connector
from dbconnector import DBConnector
from config import Config

config = Config()

# load the DB Connector to execute the creates
db = DBConnector()

# *** TABLES CONTAINING DATA WHICH IS REFRESHED EACH TIME, AND THEREFORE CAN BE DROPPED SAFELY ***
# Array containing create statements for tables.
TABLES = {}
TABLES['dailyInfected'] = (
    "CREATE TABLE `dailyInfected` ("
    "  `infected` int(11) NOT NULL,"
    "  `date` date NOT NULL,"
    "  PRIMARY KEY (`date`)"
    ") ENGINE=InnoDB")

# Loop over the array
for table_name in TABLES:
	table_description = TABLES[table_name]
	
	print("Dropping table %s if it exists" % format(table_name))
	db.executeQuery('DROP TABLE IF EXISTS %s' % str(table_name))
	
	print("Creating table %s " % format(table_name))
	db.executeQuery(table_description)

# *** TABLES FOR WHICH DATA IS NOT REFRESHED, SO THEY CAN'T BE DROPPED ***
# Array containing create statements for tables.
PERSISTENTTABLES = {}
PERSISTENTTABLES['temperatureLog'] = (
    "CREATE TABLE `temperatureLog` ("
    "  `temperature` DECIMAL(5,1) NOT NULL,"
    "  `date` datetime NOT NULL,"
    "  PRIMARY KEY (`date`)"
    ") ENGINE=InnoDB")

# Loop over the array
for table_name in PERSISTENTTABLES:
	table_description = PERSISTENTTABLES[table_name]
	
	print("Checking if table %s exists" % format(table_name))
	tableCount = db.getCount('SHOW TABLES LIKE \'%s\';' % str(table_name))
	if tableCount == 0:
		print("Creating table %s " % format(table_name))
		print(table_description)
		db.executeQuery(table_description)
	else:
		print('Table %s already exists and could contain unique data, skipping table' % format(table_name))
