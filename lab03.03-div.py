# Program to divide one number by another
# displaying the integer result and remainder

first = int(input("The number is: "))
divideby = int(input("To be divided by: "))

result = int(first / divideby)
remainder = first % divideby

print("The result is:" + str(result), "with remainder:" + str(remainder))
