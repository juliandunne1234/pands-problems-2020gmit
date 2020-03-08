# Calculate the suare root of a positive 
# floating point no. using python.
def sqrt():
    
    enternumber = float(input("Please enter number: "))
    squareroot = round(enternumber ** 0.5, 6)
    print("The square root of", enternumber, "is approx.", squareroot)

sqrt()