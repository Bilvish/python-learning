# Lists

numbers = [10, 20, 30, 40, 50]

# Accessing items
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])

# Changing an item
numbers[0] = 100
print(numbers)

# Adding items
numbers.append(60)
numbers.insert(1, 15)

# Removing items
numbers.remove(30)
numbers.pop()

# Useful functions
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Loop through a list
for number in numbers:
    print(number)