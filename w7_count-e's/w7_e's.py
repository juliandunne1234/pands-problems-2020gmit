#Program that read a Moby Dick text file
#and counts the number of times the letter
#e appears in it.
e_count = 0

filename = 'moby_dick.txt'

with open (filename, 'r') as myfile:
    
    words = myfile.read().lower()
    for e_letter in words:
        if e_letter == 'e':
            e_count += 1

print("The letter e appears {} times in this copy of Moby Dick"
.format(e_count))










