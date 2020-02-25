#This program stores a students info
#Including name, modules taken & grading.
#It then prints out this info.
student_file = {
    'student': 'mary',
    'courses': [{'module':'programming',
    'grade':45},
    {'module':'history',
    'grade':99}]
    }

print ("student:", student_file['student'])
for course in student_file['courses']:
    print(course['module'], course['grade'])

