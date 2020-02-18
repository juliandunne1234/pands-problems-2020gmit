# Program will continue to read student names
# until blank "" is entered.

# Names list
names = []

# Enter a name then check if it is blank"" in the while loop
first_name = input("enter first name ("" to quit): ").strip()

while first_name != "":
    student = {}
    student['first_name'] = first_name
    last_name = input("enter surname ("" to quit): ").strip()
    student['last_name'] = last_name
    names.append(student)

    # next student
    first_name = input("enter first name of next student ("" to quit): ").strip()

print ("Here are the student names entered:")
for student_name in names:
    print (student_name['first_name'], student_name['last_name'])
