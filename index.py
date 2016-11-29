from Fast_Brain import FastBrain
from Slow_Brain import SlowBrain

user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'

def brain(input):
    SB = SlowBrain()
    FB = FastBrain(user, password, host, database)
    FBsearch = FB.FBsearch(input) # run a fast brain search

    if FBsearch == True:
        FB.printFB() # print all fast brain values
        return True
    else:
        x = SB.SBPrimeDetermination(input)
        FB.printFB() # print all fast brain values
        return x

#quick test of our brain function
# for x in range (10000,50000):
#     brain(x)
#
# for x in range (10000,50000):
#     brain(x)

#brain(8)