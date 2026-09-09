# Create and write data

with open("students.txt", "w") as file:
    file.write("Name,Marks\n")
    file.write("Lavish,85\n")
    file.write("Rahul,72\n")
    file.write("Aman,91\n")
    file.write("Priya,64\n")


# Read and process data

try:
    with open("students.txt", "r") as file:

        header = next(file)

        for line in file:
            name, marks = line.strip().split(",")

            marks = int(marks)

            if marks >= 75:
                result = "Good"
            else:
                result = "Needs Improvement"

            print(name, marks, result)

except FileNotFoundError:
    print("File not found")