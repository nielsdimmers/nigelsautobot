import mysql.connector
import config

database = mysql.connector.connect(host=config.DBHOST,database=config.DBNAME,user=config.DBUSER,password=config.DBPASSWD)

cursor = database.cursor()

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
	try:
		print("Dropping table {} if it exists".format(table_name))
		cursor.execute('DROP TABLE IF EXISTS '+str(table_name))
		print("Creating table {}: ".format(table_name), end='')
		cursor.execute(table_description)
	except mysql.connector.Error as err:
		print(err.msg)
	else:
		print("OK")

cursor.close()
database.close()