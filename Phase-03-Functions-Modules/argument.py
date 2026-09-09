# Function Arguments and Return Values

# Positional arguments
def add(a, b):
    return a + b

print(add(10, 20))


# Keyword arguments
def student(name, age):
    return f"{name} is {age} years old"

print(student(age=20, name="Lavish"))


# Default argument
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Lavish")


# Variable-length arguments
def average(*marks):
    return sum(marks) / len(marks)

print(average(80, 90, 75, 85, 70))