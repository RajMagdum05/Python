## If statement
#python have indentation means by default it will give you spaces so code looks clean

age = int(input("Enter your age: "))

if age>=18:   #dont give { }
    print("You are an adult")
elif age>14 and age<18:  # elif means else if here
    print("Teenager")
else:
    print("Child")

age == 100 #equal to

# if is correct then it will execute that block and breaks the block without checking remaining blocks
# so to check futhur blocks write if instead of elif, it will check that to


##Logical operators (and, or, not)
#used to check if two or more conditional statements are true
 # and -> both conditions needs to be true for true
 # or -> any one is true then it will be true
 # not -> makes it opposite
 # not(True) = False
temp = int(input("Enter Temperature: "))
