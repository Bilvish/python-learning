try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")



try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)





try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")



age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")