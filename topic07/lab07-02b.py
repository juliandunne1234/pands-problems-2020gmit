#Function that takes a number from a file 
#and overwrites it

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

writeNumber(344)