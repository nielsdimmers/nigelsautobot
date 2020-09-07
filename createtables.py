import mysql.connector
import config

database = mysql.connector.connect(host=config.DBHOST,database=config.DBNAME,user=config.DBUSER,password=config.DBPASSWD)

cursor = database.cursor()

# This is a stub.
# TABLES = {}
# TABLES['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")

# try:
#   print("Creating table {}: ".format(table_name), end='')
#   cursor.execute(table_description)
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#     print("already exists.")
#   else:
#     print(err.msg)
# else:
#   print("OK")

cursor.close()
database.close()