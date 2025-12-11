# Functions in Python

# Basic function
def greet_farooq():
    print("Hello Farooq, welcome to Python programming!")

greet_farooq()


# Function with parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Sum =", result)


# Function using Farooq's information
def introduce_farooq(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

introduce_farooq("Farooq Shah", 23, "Abbottabad")


# Function returning multiple values
def farooq_scores():
    english = 85
    programming = 90
    return english, programming

eng, prog = farooq_scores()
print("Farooq's English Score:", eng)
print("Farooq's Programming Score:", prog)





# Lambda Functions in Python

# Basic lambda
square = lambda x: x * x
print(square(5))

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(10, 20))

# Lambda using Farooq's data
farooq_age_in_future = lambda current_age: current_age + 5
print("Farooq's age after 5 years:", farooq_age_in_future(23))

# Lambda inside another function
def multiplier(n):
    return lambda x: x * n

times_three = multiplier(3)
print("Farooq's productivity * 3 =", times_three(10))
