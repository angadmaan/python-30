# Strings in Python are sequences of characters enclosed in either single quotes (' ') or double quotes (" "). They are used to represent text data and can include letters, numbers, symbols, and whitespace. Strings are immutable, meaning that once they are created, their content cannot be changed.

# You can create strings in Python using single quotes, double quotes, or triple quotes (for multi-line strings).

# Single quotes

string1 = 'Hello, World!'   

# Double quotes

string2 = "Python is fun!"

# Triple quotes (for multi-line strings)

string3 = '''This is a multi-line string.
It can span multiple lines.'''  

print(string1)  # Output: Hello, World!
print(string2)  # Output: Python is fun!
print(string3)  # Output: This is a multi-line string. It can span multiple lines.

# String slicing 

# You can access individual characters or substrings in a string using slicing. The syntax for slicing is string[start:end], where start is the index of the first character to include, and end is the index of the first character to exclude.

# Example of string slicing

my_string = "Hello, Python!"

# Accessing individual characters   

first_character = my_string[0]  # 'H'

last_character = my_string[-1]  # '!'

# Slicing a substring

substring = my_string[7:13]  # 'Python' 

print(first_character)  # 'H'
print(last_character)  # '!'
print(substring)  # 'Python'

# Slicing with skip values

# You can also specify a step value in slicing to skip characters. The syntax for this is string[start:end:step].

word = "Python Programming"

skipped_chars = word[0:17:2]  # 'Pto rgamng'

print(skipped_chars)  # 'Pto rgamng'

# String functions  

# 1. len(): This function returns the length of a string.

length = len(my_string)

print(length)  # Output: 14

# 2. upper(): This function converts all characters in a string to uppercase.

uppercase_string = my_string.upper()

print(uppercase_string)  # Output: HELLO, PYTHON!

# 3. lower(): This function converts all characters in a string to lowercase.

lowercase_string = my_string.lower()

print(lowercase_string)  # Output: hello, python!

# 4. count(): This function counts the number of occurrences of a substring in a string.

count_occurrences = my_string.count('o')

print(count_occurrences)  # Output: 2

# 5. find(): This function returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.

index_of_substring = my_string.find('Python')

print(index_of_substring)  # Output: 7

# 6. replace(): This function replaces occurrences of a substring with another substring.

new_string = my_string.replace('Python', 'Java')

print(new_string)  # Output: Hello, Java!

# 7. capalize(): This function capitalizes the first character of a string and converts the rest to lowercase.

capitalized_string = my_string.capitalize()

print(capitalized_string)  # Output: Hello, python!

# Escape Sequences Characters

print("Hello, World!")  # Output: Hello, World!

print("Hello,\nWorld!")  # Output: Hello, # World! (new line)

print("Hello,\tWorld!")  # Output: Hello,    World! (tab space)

print("Hello, \"World\"!")  # Output: Hello, "World"! (double quotes inside string)

print("Hello, \\World!")  # Output: Hello, \World! (backslash inside string)
