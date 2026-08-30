# Type Casting

x = "25"
y = "10.5"

a = int(x)
b = float(y)

print(a)
print(b)

# Convert number to string
age = 20
message = "My age is " + str(age)
print(message)

# Type checking
print(type(a))
print(type(b))
print(type(message))

# Input + type casting
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)