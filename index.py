from Database import Database
from Fast_Brain import FastBrain
from Slow_Brain import SlowBrain


user = 'root'
password = '1991'
host = 'localhost'
database = 'TEST_DB'


def brain(input):
    SB = SlowBrain()
    FB = FastBrain(user, password, host, database)

    if FB.FBsearch(input) == True:
        print("its in the FB ======> " + str(FB.FBsearch(input)))
    else:
        print("using the SB ======> " + str(SB.SBPrimeDetermination(input)))
        FB.addit()



input = 5
brain(input)