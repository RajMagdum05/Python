# printing in python
print("Hello World") #don't include ; in python
print("It's really good!!")

#Variables in python
#String cant perform normally math on string
name = "Bro" #or 'Bro' string 
print(name) #Bro
print("name") #name so whatever is there in "" it will print as it is

print("Hello "+name) # Hello Bro
print(f"Hello {name}") # f means formatting use { } placeholder when f is used
#use f to write vaiable inside " " using { }
# use f string if you are going to have variable inside print

#to see datatype of a variable
print(type(name)) # use type function

#we can combine or add same datatype variables
#it cant combine string with int or any other datatype, string with string only
#Concatenation
first_name = "Raj"
last_name = "Magdum"
full_name = first_name + last_name
print("Hello "+full_name) #Hello Raj Magdum

#int datatype
age = 21
age = age+1 #age += 1
print(age) #22
print(type(age))
#print("Your age is: "+age) #this will give you error
#bcz here we are trying to concatenate string with int age
#so we need to do type casting here
print("Your age is: "+str(age)) #this makes age in string and print it like that

#float dataype decimal no.
height = 250.5
print(height) #250.5
print("Your height is: "+str(height)+(" cm")) #Your height is: 250.5 cm

#boolean
human = True #T and F are capital
being = False # no "" bcz it will become string
print("Are you a human: "+str(human)) # True
print(type(human)) # bool

name = "Raj"
name = bool(name)
print(name) #it will print True
# so whatever is there in "" it will print True, if it is empty then only it prints False
# so we can use this while taking name as input from user, so if he skips it then it will return false and msg like enter your name can be print
name = input("Enter your Name: ")
is_valid = bool(name)
if is_valid:
    print(f"Your name is {name}")
else:
    print("Enter Your name to proceed!")


##Multiple Assignment variables in one line

#For different datatypes or same datatype but different values
name, age, attractive = "Raj", 21, True

#for same values
raj = prasad = parth = 20 # so all have same value of same datatype

#String methods
name = "bro Code"

print(len(name)) #prints length of variable including spaces
print(name.find("o")) # returns index which starts from 0 from left
# so here it is 2 for o and 3 for space btw

print(name.capitalize())
#so it will capitalize only first letter in string and remaining all to small 
# bro Code -> Bro code it will make C to c

print(name.upper())
#makes all letters to upper case
# bro code -> BRO CODE

print(name.lower())
#makes all ltters to lower case
#Bro Code or BRO CODE -> bro code

print(name.isdigit())
#sees if string has digits and returns bool
# name = "123" if yes-> True no then false
# name = "Bro Code" -> False
# name = "123" -> True

print(name.isalpha())
#sees string has all alphabets returns bool
#name = "BroCode" -> true
#name = "Bro Code" -> False bcz space is there so it needs all the things to be alphabetical
#name = "123" -> False

print(name.count("o")) #counts how many o is there in a string
# also counts spaces print(name.count(" "))

print(name.replace("o","a"))
#it replaces o with a

print((name)*3) 
# name = Bro
# BroBroBro cant use \n
# name = "3"
# print(name*3) -> 333 so we cant normally perform math on string
# We need to typecast it to int
# print(int(name)*3) -> 9

##Type Casting
# int and float to string is needed when 
#print("x is: "+ str(x))
x = 1
y = 2.0
z = "3"
x = str(x)
y = int(y)
z = float(z*3) #333.0 first z*3 = 333 then make that to float 333.0
print(x,y,z) # it will print all in one row having space btw them
#for z*3 do that in print statement

 
 ## User Input in python
name = input("What is your name: ")
age = int(input("How old are you: "))
height = float(input("How tall are you: ")) #175 ->175.0 ghety

# so age and height will store that input as astring so to store it in int or float we need to typecast them respectively.
age += 1
print("Hello "+name)
print("You are "+str(age)+" years old.")
print("You are "+str(height)+" cm tall.")
#so for string everything is fine but for int and float we need to typecast it while taking input
#otherwise it will take int like 3 in string format only
# no need to do that for string

## useful functions related to numbers

import math #inlcude this library
pi = 3.7
x=10
y=23
z=12

print(round(pi)) #rounded off to nearest integer
# pi = 3.14 -> 3 # pi = 3.8 -> 4 # less that 0.5 ->3 and more then 4, for exact 3.5 -> 4

print(math.ceil(pi)) #it gives ceiling means upper value
#for upper nearest no.
#3.14 -> 4

print(math.floor(pi)) #it gives floor means lower value
#for lower nearest no.
#3.14 -> 3, 3.7-> 3

print(abs(pi)) #gives mod 
#-3.14 -> 3.14

print(pow(pi,2)) # pi to the power 2

print(math.sqrt(pi)) # square root

print(max(x,y,z)) # gives max among all

print(min(x,y,z)) #gives min among all


## String Slicing - create sub-string
# indexing[] or slice[]
#[strating index : stopping index]
name = "Raj Magdum"
#       0123456789
print(name[0]) # R
print(name[2]) # j
print(name[3]) #  it just prints space

print(name[0:2]) # Ra
# it will include 0 but not 2
# so read it like start from 0 upto 2 but not include 2
print(name[:3]) # Raj
#so it will be fine if we not give starting index, it will start from index 0.

print(name[4:10]) # Magdum
print(name[4:]) # Magdum upto end

print(name[0:10:2]) # so start with index 0 and take every 2nd character
#this 2 refers to step
#print[::2] # R gm
#means R then skip 1, skip 2 and then 3 print it like that

#Reverse Slicing Negative Indexing
#print[::-1] # it will start printing opp
#  name = "R   a  j     M  a  g  d  u  m"
#         -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# so it will print mudgaM jaR

## Using slice() function and Negative indexing
website1 = "http://google.com"
website2 = "http://wikipedia.com"

print(website1[slice(7,-4)]); #to print only google
# or slice = slice(7,-4) and print(website1(slice))
# we can use positive and negative indexing at a time
slice = slice(7,-4);
print(website2[slice]);

