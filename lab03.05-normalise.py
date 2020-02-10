# Stripping leading or trailing spaces
# from a string and displaying in lower case.
# Outputs length of original and normalised string.

string_entry = input("String to be entered: ")
string_stripping = string_entry.strip().lower()

original_length = len(string_entry)
revised_length = len(string_stripping)

print("The string after stripping is: " + string_stripping)

print("The length of string changed from " + str(original_length) + 
" to a string length of " + str(revised_length))
