
def brain(input):
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for x in list:
        if x == input:
            return True
    return False

#print (brain(17))