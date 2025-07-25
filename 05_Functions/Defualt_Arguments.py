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
def count(end, start=0): # we can do this
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE !!")

#print(count(10))

##KeyWord Arguments - an argument preceded by an identifier
# helps with readability
# order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title = "Mr", first = "Raj", last = "Magdum" )
# as we can change the order also but "Hello" i.e. positional argument's order should be correct

hello("Hello", first = "Raj", last = "Magdum", title = "Mr") # it will print in order with function print statement

for x in range(1, 11):
    print(x, end = " ") # here end is keyword
print()

print("1", "2", "3", "4", "5", sep = "-") # seperate keyword


## Arbitrary Arguments
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * is unpacking operator

# *args -> Arbitrary positional arguments
# **kwargs -> Arbitrary Key-Wrod Arguments

def add(*args): # name i.e. args can be different
    print(type(args)) # tuple means it takes the parameters and store it to tuple
    total = 0
    for arg in args:
        total+=arg
    return total


print(add(1,2,3)) # now here there is no need to give parameters, so we can add any no. of parameters.

# To display parameters in function taking args parameter we need to run for loop
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.", "Raj", "Magdum", 6844)


## kwargs
def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "Rajwada Road",
              building_name = "Rajwada",
              city = "Ich",
              state = "MH",
              pincode = "416143")
# so these are stored and returned in key, value pair as dictionary

## We can pass both *args and **kwargs in a function

def shipping_table(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
     

shipping_table("Hello", "Raj", "Magdum", "6844",
               city="Ich",
               street="Rajwada Road",
               pincode="416143",
               building="Rajwada")