# Modules in Python

# Importing a built-in module
import math

print("Square root of 49 =", math.sqrt(49))
print("Value of pi =", math.pi)


# Importing specific functions from a module
from random import randint

print("Random number for Farooq =", randint(1, 100))


# Renaming modules using alias
import datetime as dt

current_time = dt.datetime.now()
print("Current time for Farooq:", current_time)


