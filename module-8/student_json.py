# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: July 27, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 8.2 Assignment
# Description: Loads student information from a JSON file, displays the
# original student list, adds a new student, displays the updated list,
# and saves the updated information back to the JSON file.

import json
from pathlib import Path



def print_students(student_list):
    # Print each student's information from the list
    for student in student_list:
        print(
            f"{student['F_Name']} {student['L_Name']}, "
            f"ID = {student['Student_ID']}, "
            f"Email = {student['Email']}"
        )


if __name__ == "__main__":
    file_path = Path(__file__).parent / "Student.json"

    #Open and load the original student data
    with open(file_path, "r") as student_file:
        students = json.load(student_file)

    print("This is the original Student list.")
    print_students(students)

    # Create and append a new student.
    new_student = {
        "F_Name": "Alice",
        "L_Name": "Wonderland",
        "Student_ID": 12345,
        "Email": "awonderland@gmail.com"
    }

    students.append(new_student)

    print("\nThis is the updated Student list.")
    print_students(students)

    # Save the updated list to the JSON file.
    with open(file_path, "w") as student_file:
        json.dump(students, student_file, indent=4)

    print("\nThe Student file has been updated.")