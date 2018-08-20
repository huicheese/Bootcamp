date_input = input("Enter DOB (d/m/y)")
parts = date_input.split("/") # this will be a list of strings
my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
print(my_dob)


