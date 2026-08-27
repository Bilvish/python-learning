# Tuples

numbers = (10, 20, 30, 40, 20)

# Accessing
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])

# Tuple functions
print(len(numbers))
print(numbers.count(20))
print(numbers.index(30))

# Loop
for number in numbers:
    print(number)

# Tuple unpacking
name, age, city = ("Lavish", 20, "Delhi")

print(name)
print(age)
print(city)