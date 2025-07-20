## Arithematic operator
# a = int(input("Enter a: "))
# a += 1 # a=a+1
# a -= 1 # a=a-1
# a *= 3 # a=a*3
# a /= 2 #a=a/2
# a %= 2 #a=a%2
# a = a**2 # a to the power 2
# a **= 2 

## If statement
#python have indentation means by default it will give you spaces so code looks clean

#1
# age = int(input("Enter your age: "))

# if age >= 18:   #dont give { }
#     print("You are an adult")
# elif age > 14 and age < 18:  # elif means else if here
#     print("Teenager")
# else:
#     print("Child")
# # == equal to operator

#2
# response = input("Would you like food? (Y/N): ")
# if response == "Y":
#     print("Have some food!")
# else:
#     print("Dont have food!")

#3
name = input("Enter your name: ")
if name == "":
    print("You did not entered your name")
else:
    print(f"Hello {name} !")

#3 Boolean in if
online = True

if online:
    print("User is online")
else:
    print("User is offline")

# if is correct then it will execute that block and breaks the block without checking remaining blocks
# so to check futhur blocks write if instead of elif, it will check that to

#Temp Convertor
unit = input("Enter unit of Temperature (°C or °F): ").lower()
temp = float(input("Enter Temperature: "));

if unit == "c":
    print(f"Temperature in °F is {round(temp * (9/5) +32, 1)} °F")
elif unit == "f":
    print(f"Temperature in °C is {round((temp-32) * (5/9), 1)} °C")
else:
    print(f"{unit} is not valid!!")

## Conditional Expressions - 
# one - line shortcut for the if-else (Ternary Operator)
# X if condition else Y

#elif is not allowed in ternary statement
num = 20
marks = 45
a=6
b=7
age = 21
temp = 50
user_role = "guest"

print("Positive" if num>0 else "Negative")
result = "Fail" if marks<35 else "Pass"
max_num = a if a>b else b
min_num = a if a<b else b
status = "Adult" if age>=18 else "Child"
weather = "Hot" if temp>40 else "Cold"
access_level = "Full access" if user_role = "admin" else "Limited access"

print(result)