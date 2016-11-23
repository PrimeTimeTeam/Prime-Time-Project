from Database import Database

user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'


print("---------------------admin------------------------")
DB = Database(user, password, host, database) # using test key
DB.connect()
DB.printAll()
#DB.input(778)
#DB.flush()