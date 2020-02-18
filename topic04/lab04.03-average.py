# Program will continue to read numbers
# and show the average until 0 is used 
# to end the loop. A While loop is used
# instead of a for loop so it continues
# to execute until the 0 condition is met.

# Empty list
numbers = []

# Enter number then check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != 0:
    
    numbers.append(number)
    
    # read the next number and check if 0 entered
    number = int(input("enter another (0 to quit): "))

for number in numbers:
    print (number)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print ("The average is", average)
