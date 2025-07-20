# # while loop -> Execute some code while some condition remains true

# #while something is true:
# #    print this
# #exits

# #1
# name = input("Enter Your name: ")

# while name == "":
#     print("Name can't be skipped")
#     name = input("Enter Your name: ") # this statement is to break out of infinte loop
# print(f"Hello {name}")

# #2
# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You Like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("Bye")

# #3
# age = int(input("Enter Your name: "))

# while age < 0:
#     print("Your Age can't be -ve")
#     age = int(input("Enter Your name: "))
# print(f"Your age is {age}")

#4
num = int(input("Enter a no. from 1-10: "))
# while condition is true loop will execute so we need to break out of it bcz ending condition is not given
while num<1 or num>10:
    print(f"{num} cannot be valid!")
    num = int(input("Enter a no. from 1-10: "))

print(f"{num}")


## For Loops - execute a block of code a fixed no. ot times
# can iterate over range, string, sequence, etc
no = 6
for x in range(no): #it start from 0 to 5
    print(x) # Means we directly give variable name here

for x in range(1,11): #starts from 1 but doesn't include 11 upto 10 only
    print(x)          # iterate 1 place 

for x in range(1,11,2): #same as i = i+2
    print(x)

for x in reversed(range(1,11,3)): #to print in reverse
    print(x)

credit_card = "1234-5678-9876-2341"

for x in credit_card: # it will print each char in new line automatically
    print(x)          #bcz print() function auto adds new line
   
# if i want to print it in one line
for x in credit_card:
    print(x, end='') # I can give spaces here if i want 

#Continue - if i want to skip something and continue from furthur
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)   #so it will print 1 to 20 except 13

# Break - if i want to break and get out of loop
for x in range(1,21,2):
    if x == 12:
        break
    else:
        print(x)  # so now here 12 will not come bcs we are iterating by 2 places.
        # means 1 3 5 7 9 11 13 15 17 19 so here 12 will not come then it wont break
        # otherwise it can

## Nested loops - loop inside a loop

for x in range(3):  # Execute this block for 3 times
    for y in range(0,10):
        print(y, end=" ")
    print()
