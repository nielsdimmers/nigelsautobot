# This script is meant to be executed once to create the tables in the database.
# It creates the table, at this moment, no data is persistent so this script can easily be
# re-run without any issues, just run refreshCovidData.py after it.
# @author Niels Dimmers
import mysql.connector
from dbconnector import DBConnector

# load the DB Connector to execute the creates
db = DBConnector()

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
