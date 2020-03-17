#Program that writes dict to a file as JSON
#Function doLoad added since previous program
#and allows operator to load dict to the terminal

import json

students = []

filename = "students.json"

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def readDict():
    #this will throw an error if the file does not exist
    with open(filename) as f:
        return json.load(f)
    

# Selection tree for program.
def selectionMenu():
    print("Choose one of the following:")
    print("\t(a)Add student")
    print("\t(v)View student")
    print("\t(l) Load students")
    print("\t(s) Save students")
    print("\t(q)Quit")
    decision = input("Type one letter (a/v/q):").strip()
    return decision

#Module name and grade.
def readModules():
    modules = []
    moduleName = input("\t\tEnter the module: ")

    while moduleName != "":
        module = {}
        module['name'] = moduleName
        module['grade'] = input("\t\tEnter the grade: ")
        modules.append(module)
        moduleName = input("\t\tEnter the next module: ").strip()
    return modules

#Function that uses dictionary for key, value pairs. 
def doAdd():
    student = {}
    student["name"] = input("\tEnter student name: ")
    student["modules"] = readModules()
    students.append(student)

#Function that uses for loop to print out module name and grade.
def displayModules(modules):
    print("\t\tName\tGrade")
    for module in modules:
        print("\t\t" + module['name'] + "\t" + module['grade'])

#Funtion that uses for loop to print student name and includes module function inside.
def doView():
    print("Students")
    for currentStudent in students:
        print("\t" + currentStudent["name"])
        displayModules(currentStudent["modules"])

def doSave():
    writeDict(students)
    print("students saved")

def doLoad():
    #We are changing global variable students
    #so need to indicate this
    global students
    students = readDict()
    print("students loaded")

#main program
choice = selectionMenu()

while choice != 'q':
 
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 'l':
        doLoad()
    elif choice == 's':
        doSave()
    else:
        print("please select either a,v,l,s or q")
    
    choice = selectionMenu()   