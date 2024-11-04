#!/usr/bin/env python3.12
def main():
    # Create an empty dictionary to store student information
    student_information = {}

    # Adding students to the dictionary
    student_information["Adair"] = {"ID": 1, "GPA": 3.4, "Credits Completed": 144.0, "Grades": [100, 95, 97, 93, 98]}
    student_information["Oracio"] = {"ID": 2, "GPA": 3.8, "Credits Completed": 75.0, "Grades": [84, 92, 94, 99, 88]}

    # Print the dictionary containing all student information
    print(student_information)    
    print()

    # List of Students
    print("List of Students")
    for student in student_information:
        print(student)
        print()

    # Print student information in a formatted way
    print("Student Information")
    print(f"Student\tID\tGPA\tCredits Completed\tGrades")
    for student, information in student_information.items():
        print(f"{student}\t{information['ID']}\t{information['GPA']}\t{information['Credits Completed']}\t\t\t{information['Grades']}")
        print()

    # Accessing Student Information Using the Key in a Loop
    print("Accessing Student Information")
    for student, information in student_information.items():
        print(f"{student} {information}")
    print()

    # Removing a student
    print("Oracio has dropped out, removing from student information registry")
    student_information.pop("Oracio")
    print(student_information)
    print()

    # Getting GPA for a specific student
    print("Getting Adair's GPA")
    print(student_information["Adair"]["GPA"])
    print()

    # Clearing the student registry
    print("Students have graduated, clearing the student registry")
    student_information.clear()
    print(student_information)

if __name__ == "__main__":
    main()

print("Completed by, Adair Salinas")