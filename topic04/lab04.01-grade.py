# This program reads a students
# exam result and determines
# if they have to repeat
# the test.

x = float(input("Please enter your exam result: "))

if x < 0 or x > 100:
    print("Please re-execute code with correct test result.")
elif x < 40:
    print("You scored a percentage of: ", x)
    print("That is a Fail")
elif x >= 40 and x < 50:
   print("You scored a percentage of: ", x)
   print("That is a Pass")
elif x >= 50 and x < 60:
    print("You scored a percentage of: ", x)
    print("That is a Merit2")
elif x >= 60 and x < 70:
    print("You scored a percentage of: ", x)
    print("That is a Merit1")
else:
    print("You scored a percentage of: ", x)
    print("That is a Distinction")
