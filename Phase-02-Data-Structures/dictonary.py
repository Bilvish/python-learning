# Dictionary

student = {
    "name": "Lavish",
    "age": 20,
    "marks": 85
}

# Accessing values
print(student["name"])
print(student.get("marks"))

# Adding and updating
student["city"] = "Delhi"
student["marks"] = 90

# Removing
student.pop("age")

# Keys and values
print(student.keys())
print(student.values())
print(student.items())

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)