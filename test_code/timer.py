import time
import math

def test(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        x = math.sqrt(number)
        x = int(x) #Rounds number down so system doesn't work for numbers who's suqare root is or rounds down to 3
        y = 3
        z=0.0
        for i in range(3, x):
            z = number % i
            y += 1
            if z==0:
                return "Not Prime"
            if y == x:
                return "Prime"
                 

start = time.time()
print(test(491))
end = time.time()
print(end - start)
