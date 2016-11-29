#DATABASE SCHEMA
#Database => TEST_DB
#Table => test_table
#Column=> a (int), SBtime (double), FBtime (double)

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
        # this method will connect us to the db
        try:
            key = mysql.connector.connect(user = self.user, password = self.password , host = self.host, database = self.database)
            print ("   Success: Connected to Database")  # success
            return key
        except mysql.connector.Error as e:  # fail ... what's the issue?
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("   Something is wrong with the username or password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("   Database doesn't exist")
            else:
                print(e)

    def StorePrimeFBtime(self, prime, FBtime):
        # this method will store the prime number and fast brain time in the database
        key = self.connect()

        mycursor = key.cursor()

        print ("   Processing: Inserting prime number & FBtime into Database...")
        addNum = ("INSERT INTO test_table (a, FBtime) VALUES (%(prime)s, %(FBtime)s)") #sql command to insert x
        X = {'prime' : prime, 'FBtime' : FBtime}
        mycursor.execute(addNum, X)
        print ("   Success: Prime number & FBtime inserted into Database")

        key.commit()
        mycursor.close()
        key.close()
        return

    def StorePrimeSBtime(self, prime, SBtime):
        key = self.connect()

        mycursor = key.cursor()

        print ("   Processing: Inserting prime number & SBtime into Database...")
        addNum = ("INSERT INTO test_table (a, SBtime) VALUES (%(prime)s, %(SBtime)s)") #sql command to insert SBtime & prime
        X = {'prime' : prime, 'SBtime' : SBtime}
        mycursor.execute(addNum, X)
        print ("   Success: Prime number & SBtime inserted into Database")

        key.commit()
        mycursor.close()
        key.close()
        return

    def appendFBtime(self, prime, FBtime):
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: appending FBtime of ( " , prime , ") ...")

        append = ("UPDATE test_table SET FBtime = %s WHERE a = %s")
        X = (FBtime, prime)
        mycursor.execute(append, X)

        key.commit()
        mycursor.close()
        key.close()

    def remove (self, num):
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: Deleting number from Database...")

        delNum = ("DELETE FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num} # used a dic. incase we want to input multi. values
        mycursor.execute(delNum, X)

        print ("   Success: Number deleted from Database")

        key.commit()
        mycursor.close()
        key.close()

    def search(self, num):
        # this method will search for a number in the database
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: searching for number (", num , ") in Database...")

        seaNum = ("SELECT a FROM test_table WHERE a = (%(x)s);") #sql command to insert x
        X = {'x' : num}
        mycursor.execute(seaNum, X)

        found = mycursor.fetchone()

        if found == None:
            print ("[ Not found ]")
            return False
        else:
            print("[ Found " + str(found[0]), " ]")
            return True

        print ("   Success: Number searched from Database")

    def printAll (self):
        #to print all prime values
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: Printing...")

        mycursor.execute("USE TEST_DB")  # select the database
        mycursor.execute("SELECT a from test_table")  # execute 'SHOW TABLES' (but data is not returned)

        for (test_table) in mycursor:
            print(str(test_table[0]), ", ", end="")

        print ("\n   Success: Printed")

        key.commit()
        mycursor.close()
        key.close()

    def flush(self):
        # this method will delete all rows in the database
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: Deleting all numbers from Database...")

        delNum = ("Truncate table test_table") #
        mycursor.execute(delNum)

        print ("   Success: Numbers deleted from Database")

        key.commit()
        mycursor.close()
        key.close()

    def last (self): # Get the last prime number inputted into the database
                     # This will only work if we give each entry an order number
                     # In this case, column num increase by 1 for each input
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: searching for last input in Database...")

        seaNum = ("SELECT a FROM test_table ORDER BY num DESC LIMIT 1;") #sql command to insert x
        mycursor.execute(seaNum)

        found = mycursor.fetchone()

        print("Found " + str(found[0]))
        return int(found[0])

    def last2 (self): # Get the last number id inputted into the database
                     # This will only work if we give each entry an order number
                     # In this case, column num increase by 1 for each input
        key = self.connect()
        mycursor = key.cursor()

        print ("   Processing: searching for last input in Database...")

        seaNum = ("SELECT num FROM test_table ORDER BY num DESC LIMIT 1;") #sql command to insert x
        mycursor.execute(seaNum)

        found = mycursor.fetchone()

        print("Found " + str(found[0]))
        return int(found[0])

    # def StorePrime (self, num):
    #     key = self.connect()
    #
    #     mycursor = key.cursor()
    #
    #     print ("  Processing: Inserting prime number into Database...")
    #     addNum = ("INSERT INTO test_table (a) VALUES (%(x)s)") #sql command to insert x
    #     X = {'x' : num} # used a dic. incase we want to input multi. values
    #     mycursor.execute(addNum, X)
    #     print ("  Success: Number inserted into Database")
    #
    #     key.commit()
    #     mycursor.close()
    #     key.close()
    #     return
    #
    #
    # def StoreFBTime (self, fbtime):
    #     key = self.connect()
    #
    #     mycursor = key.cursor()
    #
    #     print ("  Processing: Inserting FBtime into Database...")
    #     addtime = ("INSERT INTO test_table (FBtime) VALUES (%(x)s)") #sql command to insert x
    #     X = {'x' : fbtime} # used a dic. incase we want to input multi. values
    #     mycursor.execute(addtime, X)
    #     print ("  Success: FBtime inserted into Database")
    #
    #     key.commit()
    #     mycursor.close()
    #     key.close()
    #
    # def StoreSBTime (self, num):
    #     key = self.connect()
    #
    #     mycursor = key.cursor()
    #
    #     print ("  Processing: Inserting SBtime into Database...")
    #     addtime = ("INSERT INTO test_table (SBtime) VALUES (%(x)s)") #sql command to insert x
    #     X = {'x' : num} # used a dic. incase we want to input multi. values
    #     mycursor.execute(addtime, X)
    #     print ("  Success: SBtime inserted into Database")
    #
    #     key.commit()
    #     mycursor.close()
    #     key.close()
    #     return
    #
    # def appendFBtime2(self, prime, FBtime):
    #     key = self.connect()
    #     mycursor = key.cursor()
    #     #self.Database(self.user, self.password , self.host, self.database)
    #     #search = self.search(prime)
    #
    #     print ("  ~~~Processing: appending FBtime for ( " , prime , ") ...")
    #
    #     #if search == True:
    #
    #     append = """    UPDATE test_table
    #                             SET FBtime = %s
    #                             WHERE a = %s """
    #
    #     X = (FBtime,prime)
    #     mycursor.execute(append, X)
    #     print ("  ~~~Success: Appended FBtime for ( " , prime , ") ...")
    #     return True
    #         #else:
    #             # print ("ERROR: The prime number isn't stored in the database... can't append")
    #             # return False
    #
    #     mycursor.close()
    #     key.close()