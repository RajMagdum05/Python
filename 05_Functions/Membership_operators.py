# Membership operators = runs the code if it is true or gives bool value
# woeks in string, list, tuple, set or dictionary
# 1. in
# 2. not in

## String
word = "APPLE"
letter = input("Guess the letter: ").upper()
if letter in word:
    print("Found")
else: 
    print("Not Found")

## Sets
students = {"Raj", "Parth", "Prasad", "Atharv"}
student = input("Enter the name of the student: ")
if student not in students:
    print("Not Found")
else:
    print("Found")

## Dictionary

grades = {"Raj": "A",
          "Om": "B",
          "Prasad": "C",
          "Atharv": "A++"}
student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")

# to get value of a key -> grades[student]
# grades[key] -> will get the value of it

email = "RajMagdum@gmail.com"

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")