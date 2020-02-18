# This code was copied from the tutorial
# as it was difficult to know how to begin it.
# Choose a random fruit from the list.

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

print("A Random Fruit:" + fruit)
