# Dictionary in python 

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# Creating a dictionary

d = {} # Empty dictionary

first = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
print(first["name"])  # Output: John    
print (first["age"])   # Output: 30
print(first["city"])  # Output: New York

# Propeties of dictionary

# 1. Dictionaries are unordered.
# 2. Dictionaries are mutable.
# 3. It is Indexed.
# 4. Values in a dictionary can be of any type.

# Dictionary Methods

print(first.keys())   # Output: dict_keys(['name', 'age', 'city'])

print(first.values()) # Output: dict_values(['John', 30, 'New York'])

first.update({"age": 31})  # Update the value of age
print(first)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

first.pop("city")  # Remove the key-value pair with key "city"
print(first)  # Output: {'name': 'John', 'age': 31}


print(first.get("name"))  # Output: John

# Diffrence between get and accessing a value using key

# If you try to access a key that does not exist using the square bracket notation, it will raise a KeyError. However, using the get() method will return None (or a specified default value) instead of raising an error.

print(first.get("city"))  # Output: None

# print(first["city"])  # This will raise a KeyError since "city" has been removed from the dictionary.

first.popitem()  # Remove the last inserted key-value pair
print(first)  # Output: {'name': 'John'}
