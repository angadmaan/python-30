# Sets in python

# A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from them.

s = set()  # Empty set

print(type(s))  # Output: <class 'set'>

# Creating a set with elements
set = {1, 2, 3, 4, 5}

print(set)  # Output: {1, 2, 3, 4, 5}

set_1 = {3, 4, 5, 6, 7, 4, 3} # Duplicate elements will be removed

print(set_1)  # Output: {3, 4, 5, 6, 7}

# Properties of sets

# 1. Sets are unordered.
# 2. Sets are mutable.
# 3. Sets do not allow duplicate elements.
# 4. Sets are unindexed.

# Operations on set

set.add(6)

print(set) 

set.remove(6)

print(set)

# set.clear()  # Empties the set 

s1 = {3, 5 , 7, 8, 10}

s2 = {12, 3, 6, 8, 14}

print(s1.union(s2))

print(s1.intersection(s2))
