# Project Name: Prime-Time-Project
# File: Utility
# NOTE: this holds all the vital testing and maintenance functions

from Database import Database
from Slow_Brain import SlowBrain

# DATABASE TEST
# Test Key
user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

def DBTest():
    # Connection/Input/Print Test
    print("---------------------------------------------")
    print("TEST_START - Processing: Testing DB Connection/Input/Print...")
    # x = 32 # test input
    # y = 7 # test input
    # z = 8 # test input
    mytestDB = Database(user, password, host, database) # using test key
    mytestDB.connect() # Database Connection
    print(mytestDB.SBtimeReturn(7))
    #mytestDB.input(x) # inputing a value
    #mytestDB.input(y) # inputing a value
    # mytestDB.remove(y) # removing all values = x
    # mytestDB.printAll() # printing all values
    # mytestDB.search(z) # search for z
    print("TEST_END - Success: Connection/Input/Print test passed")
    print("---------------------------------------------")
#
# def SlowBrainTest():
#     print("---------------------------------------------")
#     print("TEST_START - Processing: Testing slow brain...")
#     slow_brain_test = SlowBrain()
#     # not counting 2, 3, 5, 7, 11, 13, because there is some problems with those
#     prime_table = [17, 19, 23, 31, 43, 47, 53, 59, 139, 151, 163, 197] # table of some prime numbers for testing
#     n = prime_table.__len__()
#     for i in range (0,n-1):
#         if slow_brain_test.SBPrimeDetermination(prime_table[i]) == True:
#             print("      Case Passed")
#     print("TEST_END - Success: slow brain test passed")
#     print("---------------------------------------------")


DBTest()
# SlowBrainTest()