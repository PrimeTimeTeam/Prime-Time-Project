#1) Testing the "Fast_Brain" connection to db
#2) inputing an int
#
#DATABASE SCHEMA
#Database => TEST_DB
#Table => test_table
#Column=> a
#

import mysql.connector
from mysql.connector import errorcode


class Database(object):
    def __init__(self):
        self.user='root'
        self.password='1991'
        self.host='localhost'
        self.database='TEST_DB'

    def Connect(self):
        #this function will connect us to the db
        try:
            key = mysql.connector.connect(self.user, self.password , self.host, self.database)
            print ("  Success: Connected to Database")  # success
        except mysql.connector.Error as e:  # fail ... what's the issue?
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("  Something is wrong with the username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("  Database doesn't exist")
            else:
                print(e)
        return key;

    def DB_Input (self, num):
        # First we must connect to the db and give error messages when we hit issues
        key = self.Connect()

        mycursor = key.cursor()

        print ("  Processing: Inserting number into Database...")
        addNum = ("INSERT INTO test_table (a) VALUES (%(x)s)") #sql command to insert x
        X = {'x' : num} # used a dic. incase we want to input multi. values
        mycursor.execute(addNum, X)
        print ("  Success: Number inserted into Database")

        key.commit()
        mycursor.close()
        key.close
        return;

    def DB_PrintAll (self):
        #to print all
        key = self.Connect()
        mycursor = key.cursor()

        print ("  Processing: Printing...")

        mycursor.execute("USE TEST_DB")  # select the database
        mycursor.execute("SELECT a from test_table")  # execute 'SHOW TABLES' (but data is not returned)

        #tables = mycursor.fetchall()  # return data from last query

        for (test_table) in mycursor:
            print(test_table)

        print ("  Success: Printed")

        key.commit()
        mycursor.close()
        key.close
        return;

    #will add more

