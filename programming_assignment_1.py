#programming assignement 1
from pylab import *
import numpy


d = int(input("how many rolls would you like to conduct?"))
a = int(input("What is the first number you want to try to roll?"))
b = int(input("What is the second number you want to try to roll?"))
def galileo(d,a,b):
    print("Calculating")
    count_a = 0
    count_b = 0
    i = 0
    t = 1

    rolls_sum = 0
    
    for x in range(0,1000000):
        while i < d:
            rolls_sum += int(numpy.random.randint(1,7))
            i += 1
        if rolls_sum == a:
            count_a = count_a + 1
        elif rolls_sum == b:
            count_b = count_b + 1
        i = 0
        rolls_sum = 0
    

    proportion_a = count_a/1000000
    proportion_b = count_b/1000000
    print(a, proportion_a, b,proportion_b)
    if (abs(proportion_a - proportion_b) < (1/(6**d))):
        print("sum of ", a, "and", b, "are equally likely to occur")
        return
    elif (proportion_b > proportion_a):
        print(b, "is more likely to be the sum of ",d, "rolls than" ,a)
    else:
        print(a, "is more likely to be the sum of ",d, "rolls than" ,b)
galileo(d, a, b)

            
 

        
