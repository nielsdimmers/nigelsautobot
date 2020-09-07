import mysql.connector
from config import Config
from dbconnector import DBConnector
config = Config()

db = DBConnector()

# Array containing create statements for tables.
TABLES = {}
TABLES['dailyInfected'] = (
    "CREATE TABLE `dailyInfected` ("
    "  `infected` int(11) NOT NULL,"
    "  `date` date NOT NULL,"
    "  PRIMARY KEY (`date`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
	table_description = TABLES[table_name]
	print("Dropping table %s if it exists" % format(table_name))
	db.executeQuery('DROP TABLE IF EXISTS %s' % str(table_name))
	print("Creating table %s " % format(table_name))
	db.executeQuery(table_description)
