#basic usage of variables in python 
# Numbers
age = 20
height = 5.9

# Text (string)
name = "Farooq"

# Boolean
is_student = True

# Print variables
print(age)        # 20
print("Name:", name)  # Name: Farooq

# Change variable value
age = 21
print(age)        # 21



# multiple variables at once 
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30

# Assign same value
a = b = c = 100
print(a, b, c)  # 100 100 100




# using variables in operations 
 # Arithmetic with variables
a = 10
b = 5
c = a + b
print(c)  # 15

# Combine text
first_name = "Farooq"
last_name = "Shah"
full_name = first_name + " " + last_name
print(full_name)  # Farooq Shah

# Using variables in f-strings
age = 21
print(f"My name is {full_name} and I am {age} years old.")
