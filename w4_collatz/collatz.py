#This program takes a number and
# completes a calculation based
# on whether the number is even or odd.

x = int(input("Please enter any number: "))

# Even number is divided by 2;
# odd number is * 3 and then add 1.

while x != 1:

    if x == 0:
        break

    elif x % 2 == 0:
        x = x / 2

    else:
        x = (x * 3) + 1
        
    print (int(x), end=' ')
        