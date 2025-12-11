# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Printing a message using input
print("Hello " + name + "! You are " + str(age) + " years old and live in " + city + ".")

# Example using a condition with input
if age >= 18:
    print(name + ", you are eligible to vote.")
else:
    print(name + ", you are not eligible to vote yet.")
