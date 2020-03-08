# Calculate the suare root of a positive 
# floating point no. uusing the import 
# math sqrt function.

import math

def sqrt():
    enternumber = float(input("Please enter a positive number: "))
    squareroot = round(math.sqrt(enternumber), 4)
    print("The square root of", enternumber, "is approx.", squareroot)   

sqrt()

