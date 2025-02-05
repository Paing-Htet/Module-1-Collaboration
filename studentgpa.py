# Author: Paing Htet    
# File Name: student_gpa.py
# Description: This app accepts student names and GPAs and checks if the student qualifies for the Dean's List or the Honor Roll.
# It will prompt for a student's last name, first name, and GPA. It will then print a message indicating if the student qualifies for the Dean's List or the Honor Roll.
# The app will stop processing student records when the last name 'ZZZ' is entered.

lastname = input("Enter the student's last name: ")

while lastname != 'ZZZ':

    firstname = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(firstname, lastname, "qualifies for the Dean's List.")
    elif gpa >= 3.0:
        print(firstname, lastname, "qualifies for the Honor Roll.")
    else:
        print(firstname, lastname, "does not qualify for the Dean's List or the Honor Roll.")

    lastname = input("Enter the student's last name: ")