"""
	Student API(application program interface)
"""
from Student_OOP import * #import all properties from Student file
from os import system
from dbhelper import *

slist:list = []
#filename:str = "student.csv" #comma-separated-variables

def header(message: str) -> None:
    system("cls")
    global students
    students = []
    #with open(filename, "r") as f:
    #    data = f.readlines()
    #    for std in data:
    #        field = std.rstrip("\n").split(",")
    #        student = Student(field[0], field[1], field[2], field[3], field[4])
    #        students.append(student)
    print("---------------------------")
    print(message)
    print("---------------------------")
def checkid(student:Student)->bool:
            for std in students:
                if std.__eq__(student):
                    return True
            return False
def idchecker(idno):
    return idno.isdigit()
def addStudent() -> None:
    header("     Add Student")
    print()
    check = False
    while True:
        idno = input("Enter IDNO: ")
        if idchecker(idno):
            getA = getall("student")
            for line in getA:
                if str(idno) in line:
                    print(f"--Student IDNO: >>{idno}<< already Exist--")
                    return idno
            if not check:
                lastname = input("Enter LASTNAME: ")
                firstname = input("Enter FIRSTNAME: ")
                course = input("Enter COURSE: ")
                level = input("Enter LEVEL: ")
                print(addrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level))
                break
        else:
            print("\nPlease input numbers in ID\n")
            break

def findStudent()->None:
    header("     Find/Search Student")
    print()
    idno = input("Enter IDNO to search: ")
    found = False 
    searched = getrecord("student",id=idno)
    for std in searched:
            print("Student Found!")
            print()
            print(f">>{searched}<<\n")
            found = True
            break          
    if not found:
        print(f"Student #:{lastname} does not exists!")
def deleteStudent() -> None:
    header("     Delete Student")
    idno = input("Enter IDNO to delete: ")
    found = False
    dele = deleterecord("student", id=idno)
    if dele:
        print("Student has been deleted")
    else:
        print(f"Student #{idno} does not exist!")

def updateStudent()->None:
    header("     Update Student")
    
    idno = input("Enter IDNO to update: ")
	lastname = input("Enter IDNO to update: ")
	firstname = input("Enter IDNO to update: ")
	course = input("Enter IDNO to update: ")
	level = input("Enter IDNO to update: ")
	print(f"Student #{idno} does not exists!" if not updaterecord("student", idno=idno,lastname=lastname,firstname=firstname,course=course,level=level) else "Updated Successfully!" )
def displayAllStudent() -> None:
    header("     Display All Student")
    getA = getall("student")
    for s in getA:
        print(s)
        print("\n------------------------------------------------------")
    print("\tNothing follows")
def quit()->None:
	header("Program Terminated")
	

def student_updater() -> None:
    with open(filename, "w") as f:    
        for std in students:
            f.write(f"{std.__str__()}\n")

