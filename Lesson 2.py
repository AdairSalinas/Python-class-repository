first_name = "Adair" 
first_name = input("Please enter your first name:") 
last_name = "Salinas"
last_name = input("Please enter your last name:") 
current_year = int(2024)
current_year = int(input("Please enter the current year:"))
birth_year = int(1985)
birth_year = int(input("Please enter your birth year:"))
age = current_year - birth_year
print("Hello"+first_name+""+last_name +"!\nYou are "+str(age)+" years old this year.")
age += 1 
print(f"Next year, you will be {age} years old, in the year {current_year +1}.")
print("\rCompleted by, Adair Salinas")