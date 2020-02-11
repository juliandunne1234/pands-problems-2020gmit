# Creating a Dictionary Object
# with 3 attributes.

currentbook = {
    'title' :'Girl With Dragon knecklace',
    'author': 'Stiggy Larsson',
    'price' : 12.99,
}

# Print the Dictionary Object
print(currentbook)

# Author of currentbook
print("\n" + currentbook['author'])

# Adding an attribute
currentbook['IBSN'] = 13245
print("\n" + str(currentbook))

# Using a for loop to iterate
# through the dictionaries
# key, values.

for key, value in currentbook.items():
    print("\nThe key is: " + key)
    print("The value is: " + str(value))
