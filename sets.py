# Sets

numbers = {10, 20, 30, 40, 20}
print(numbers)             # Duplicate 20 is removed

# Adding
numbers.add(50)
numbers.update([60, 70])

# Removing
numbers.remove(30)
numbers.discard(100)       # No error if 100 doesn't exist

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)               # Union
print(a & b)               # Intersection
print(a - b)               # Difference
print(a ^ b)               # Symmetric difference

# Length
print(len(numbers))