#!/usr/bin/env python3.12
# imports the random function so it can be used later in the program
import random

def main():
    grades = []
    # Creates infinite loop
    while True:
        # asks and accepts user input and assigns a number to a variable
        user_grade = int(input("Enter a grade or type -1 to stop entering grades:"))
         # adds user input to the grades list
        if user_grade in range(0,101):
            grades.append(user_grade)
        # breaks the user out of the loop once they have entered all their grades
        elif user_grade == -1:
            break
        # lets the user know they input an invalid grade
        else:
            print("The grade you entered is invalid.")
    # prints the list of grades entered by user
    print(grades)
    # Heading so the user understand what is happening
    print("Removing the Lowest Grade...")
    # assigns i to find the minimum
    i = grades.index(min(grades))
    # removes lowest grade from list
    grades.pop(i)
    # prints new list with lowest grade removed
    print(grades)
    # Heading for clarity
    print("Removing a Random Grade...")
    # Function to remove a random grade
    grades.remove(random.choice(grades))
    # prints new list with random grade removed
    print(grades)
    print("Sorting and Reversing List")
    grades.sort()
    grades.reverse()
    print(grades)
    print("Getting Grade Total and Average")


    print("Edit a Grade")
    while True:
        for index, grade in enumerate(grades, start=1):
            print(f"{index}. {grade}")
            choice = input("Enter the number of the grade you would like to edit: ")
            if choice.isdigit():
                choice = int(choice)
                if 1<= choice <= len(grades):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(grades)}.") 
           
    
if __name__ == "__main__":
    main()

   