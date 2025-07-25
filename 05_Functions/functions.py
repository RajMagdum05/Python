# function - A block of reusable code
# place () after the function name

def happy_birthday(name, age): # def function_name(parameters without datatypes in python)
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old !!")
    print( )

happy_birthday("Raj", 21)
happy_birthday("Om", 30)

# return = statement used to end a function
# and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last  # return statement we can directly write + or other operartors

print(create_name("Raj", "Magdum"))

## Default Arguments = A default value for certain parameters
# it makes your functions more flexible, reduces no. of arguments
# 1. positional, 2. DEFAULT, 3. Keyword, 4. arbitrary

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1-discount) * (1+tax)

print(net_price(500)) # only list_price parameter is passed and other two is taken as default
print(net_price(500, 0.1, 0)) # now here we can pass other parameters if we want to pass different parameters
# so we pass parameters it will take that other wise it will take default when we dont pass


#E.g.
import time

#def count(start=0, end): we cant do this we need to pass only one value to end but its position is second so it will not match
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE !!")

print(count(10))
