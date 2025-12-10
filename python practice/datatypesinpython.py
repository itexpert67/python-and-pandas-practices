# ------------------------------
# Python Basic Data Types
# ------------------------------

# 1. Numbers
int_var = 10          # Integer
float_var = 5.75      # Floating-point
complex_var = 2 + 3j  # Complex number

print(int_var, type(int_var))       # 10 <class 'int'>
print(float_var, type(float_var))   # 5.75 <class 'float'>
print(complex_var, type(complex_var)) # (2+3j) <class 'complex'>

# 2. Strings
str_var = "Hello Python"
char_var = 'A'  # Single character
print(str_var, type(str_var))  # Hello Python <class 'str'>
print(char_var, type(char_var)) # A <class 'str'>

# 3. Boolean
bool_true = True
bool_false = False
print(bool_true, type(bool_true))  # True <class 'bool'>
print(bool_false, type(bool_false)) # False <class 'bool'>

# 4. Lists (ordered, mutable)
list_var = [1, 2, 3, "Python"]
print(list_var, type(list_var))  # [1, 2, 3, 'Python'] <class 'list'>

# 5. Tuples (ordered, immutable)
tuple_var = (1, 2, 3, "Python")
print(tuple_var, type(tuple_var)) # (1, 2, 3, 'Python') <class 'tuple'>

# 6. Sets (unordered, unique)
set_var = {1, 2, 3, 3, 4}
print(set_var, type(set_var)) # {1, 2, 3, 4} <class 'set'>

# 7. Dictionaries (key-value pairs)
dict_var = {"name": "Farooq", "age": 21}
print(dict_var, type(dict_var)) # {'name': 'Farooq', 'age': 21} <class 'dict'>
