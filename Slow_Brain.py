from Database import Database
import math
import time

user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

class SlowBrain(object):
    def __init__(self):
        self.number = None
        self.SBtime = 0.00

    def SBPrimeDetermination(self, d):
        self.number = d
        db = Database(user, password, host, database)

        print("Starting up Slow Brain...")

        start = time.time()

        if self.number == 1:
            print ("Slow Brain: [not prime]")
            return False

        if self.number % 2 == 0: # Is the number even?
            print ("Slow Brain: [not prime]")
            return False
        else:
            x = math.sqrt(self.number) # Find the ranges max for checking prime
            x = int(x)+1 # rounds number down
            z = 0.0 # Needs to be decimal so python doesn't round to zero
            for i in range(3, x, 2):
                z = self.number % i
                if z == 0: # If a number divides evenly
                    end = time.time()
                    self.SBtime = end - start
                    print("The SB search took ", str(self.SBtime), " seconds.")
                    print ("Slow Brain: [not prime]")
                    return False # Not Prime

            end = time.time()
            self.SBtime = end - start
            print ("Slow Brain: [prime]")
            print("The SB search took ", str(self.SBtime), " seconds.")
            db.StorePrimeSBtime(self.number,self.SBtime)
            return True # Prime

#testing
# a = SlowBrain()
# print("here" + str(a.SBPrimeDetermination(88)))
