#DATABASE SCHEMA
#Database => TEST_DB
#Table => test_table
#Column=> a (BIGINT), SBtime (DOUBLE), FBtime (DOUBLE)

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

class Database(object):
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect(self):
        #this method will connect us to the db
        try:
            key = mysql.connector.connect(user = self.user, password = self.password , host = self.host, database = self.database)
            print ("  Success: Connected to Database")  # success
        except mysql.connector.Error as e:  # fail ... what's the issue?
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("  Something is wrong with the username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("  Database doesn't exist")
            else:
                print(e)
        return key

    def StorePrimeFBtime(self, prime, FBtime):
        #this method will store a prime number and the fbtime
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Inserting prime number & FBtime into Database...")
        addNum = ("INSERT INTO test_table (a, FBtime) VALUES (%(prime)s, %(FBtime)s)") #sql command to insert x
        X = {'prime' : prime, 'FBtime' : FBtime} # used a dic. incase we want to input multi. values
        mycursor.execute(addNum, X)
        print ("  Success: Prime number & FBtime inserted into Database")

        key.commit()
        mycursor.close()
        key.close()
        return

    def StorePrimeSBtime(self, prime, SBtime):
        #this method will store a prime number and the sbtime
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Inserting prime number & SBtime into Database...")
        addNum = ("INSERT INTO test_table (a, SBtime) VALUES (%(prime)s, %(SBtime)s)")
        X = {'prime' : prime, 'SBtime' : SBtime}
        mycursor.execute(addNum, X)
        print ("  Success: Prime number & SBtime inserted into Database")

        key.commit()
        mycursor.close()
        key.close()
        return

    def appendFBtime(self, prime, FBtime):
        #this method will append the fbtime of a prime number
        key = self.connect()
        mycursor = key.cursor()

        print ("  ~~~Processing: appending FBtime of ( " , prime , ") ...")

        append = ("UPDATE test_table SET FBtime = %s WHERE a = %s")
        X = (FBtime, prime)
        mycursor.execute(append, X)

        key.commit()
        mycursor.close()
        key.close()

    def remove (self, num):
        #this method will remove a prime number
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Deleting number from Database...")

        delNum = ("DELETE FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num} # used a dic. incase we want to input multi. values
        mycursor.execute(delNum, X)

        print ("  Success: Number deleted from Database")

        key.commit()
        mycursor.close()
        key.close()

    def search(self, num):
        #this method will search for a prime number (output bool)
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for number (", num , ") in Database...")
        seaNum = ("SELECT a FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)
        found = mycursor.fetchone()

        if found == None:
            print ("Not found")
            return False
        else:
            print("Found " + str(found[0]))
            return True
        print ("  Success: Number searched from Database")


    def SBtimeReturn(self, num):
        #this method will return the sbtime of a prime number
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for number (", num , ") in Database...")

        seaNum = ("SELECT SBtime FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)

        found = mycursor.fetchone()

        if found == None:
            print ("SBtimeReturn: Not found")
            return 0
        else:
            print("SBtimeReturn: Found " + str(found[0]))
            return found[0]

        print ("  Success: Number searched from Database")

    def FBtimeReturn(self, num):
        #this method will return the fbtime of a prime number
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for number (", num , ") in Database...")

        seaNum = ("SELECT FBtime FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)

        found = mycursor.fetchone()

        if found == None:
            print ("FBtimeReturn: Not found")
            return None
        else:
            print("FBtimeReturn: Found " + str(found[0]))
            return found[0]

        print ("  Success: Number searched from Database")

    def primeReturn(self, id):
        #this method will return the prime number by using it's id
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: searching for number (", id , ") in Database...")

        seaNum = ("SELECT a FROM test_table WHERE idtest_table = (%(x)s);") #sql command to insert x
        X = {'x' : id}
        mycursor.execute(seaNum, X)
#
        found = mycursor.fetchone()

        if found == None:
            print ("primeReturn: Not found")
            return False
        else:
            print("primeReturn: Found " + str(found[0]))
            return found[0]

    def printAll (self):
        #to print all prime values
        key = self.connect()
        mycursor = key.cursor()

        print ("  Processing: Printing...")

        mycursor.execute("USE TEST_DB")
        mycursor.execute("SELECT a from test_table")

        for (test_table) in mycursor:
            print(str(test_table[0]), ", ", end="")

        print ("\n  Success: Printed")

        key.commit()
        mycursor.close()
        key.close()

    def flush(self):
        #this method will delete all values
        key = self.connect()
        mycursor = key.cursor()

        print ("      Processing: Deleting all numbers from Database...")

        delNum = ("Truncate table test_table") #
        mycursor.execute(delNum)

        print ("      Success: Numbers deleted from Database")

        key.commit()
        mycursor.close()
        key.close()