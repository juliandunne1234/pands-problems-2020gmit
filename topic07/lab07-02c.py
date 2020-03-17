#Program that uses 2 functions to count
#how many times a program has been run

filename = 'count.txt'
def readNumber():
    with open (filename) as f:
        number = int(f.read())
        return number

filename = 'count.txt'
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 1
print ("we have run this program {} times".format(num))

writeNumber(num)