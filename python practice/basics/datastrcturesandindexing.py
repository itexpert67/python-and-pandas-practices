    

'''listing'''

# Example list using your info
my_info = ["Farooq", 25, "Abbottabad", "Student"]

# Accessing elements
print(my_info[0])  # Farooq
print(my_info[1])  # 25

# Changing an element
my_info[1] = 26
print(my_info)  # ['Farooq', 26, 'Abbottabad', 'Student']

# Adding elements
my_info.append("Sociology")
print(my_info)  # ['Farooq', 26, 'Abbottabad', 'Student', 'Sociology']

# Slicing
print(my_info[1:4])  # [26, 'Abbottabad', 'Student']
  


'''tuples'''

# Example tuple
my_info_tuple = ("Farooq", 26, "Abbottabad", "Student")

# Accessing elements
print(my_info_tuple[2])  # Abbottabad

# Tuples cannot be changed
# my_info_tuple[1] = 27  # This will give an error





'''dictioniers'''

# Example dictionary
my_info_dict = {
    "name": "Farooq",
    "age": 26,
    "city": "Abbottabad",
    "department": "Sociology"
}

# Accessing values
print(my_info_dict["name"])  # Farooq

# Changing a value
my_info_dict["age"] = 27
print(my_info_dict)  # {'name': 'Farooq', 'age': 27, 'city': 'Abbottabad', 'course': 'Sociology'}

# Adding new key-value
my_info_dict["university"] = "hazara university"
print(my_info_dict)
   



'''sets'''

# Example set
my_info_set = {"Farooq", "Abbottabad", 26, "Student"}

print(my_info_set)

# Adding and removing
my_info_set.add("Sociology")
my_info_set.remove(26)
print(my_info_set)
