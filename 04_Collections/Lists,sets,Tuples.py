#Collection = single "variable" used to store multiple values
# List = [] oredered and changable, Duplicates Ok
# Set = {} unodered and immutable cant change, but Add/Remove ok, No Duplicates
# Tuple = () oredered and unchangable, Duplicates Ok, no add/remove, FASTER

## List ->
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits) #prints all [ ]
print(fruits[0]) # apple fruits[2] -> banana
print(fruits[:2]) # apple, orange
print(fruits[::-1]) #prints reverse

for fruit in fruits: #so instead of x we can use fruit here
    print(fruit)

#print(dir(fruits)) #it will print all the available functions associated in python
#print(help(fruits)) #for indepth explanation

print(len(fruits)) # prints len of list -> 4

print("apple" in fruits) # prints bool value as True or False
# True
print("Apple" in fruits) # False so case sensitive
print("pineapple" in fruits) #False

#fruits[0] = "pineapple" # we can change
#print(fruits)

fruits.append("pineapple") # so it will add this to end
print(fruits)

#fruits.remove("apple") #so it will remove that
#print(fruits)
#so print(fruits.remove("apple")) -> this will print none
#so first remove it and then print it

fruits.insert(0, "pineapple")
print(fruits) #so it will remove value from index 0 and insert pineapple there

fruits.sort()
print(fruits) # it will print alphabetically

fruits.reverse()
print(fruits) # it will reverse the list

# if we want to reverse it alphabetically then first sort it then reverse it

#fruits.clear() #it will clear entire list

print(fruits.index("pineapple")) #it will return index
# here there are 2 pineapple then it will retuen first one

print(fruits.count("banana")) # 1
print(fruits.count("pineapple")) #2

# so if we want index or to count and that to be displayed so we can use that
# satement like fruits.count() or fruits,index directly in print statement
# but for reverse, sort, append, insert we first need to do that functions and then we need to print(fruits)


## Sets -> Unodered and randomly prints 
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)  # it will randomly prints these 4 values means unordered

#print(fruits[1]) # so no indexing works here bcz odered is not fixed

#print(dir(fruits)) we can find all the functions applicable here
# can be executed same as list

fruits.add("pineapple")
print(fruits) # it will add it randomly anywhere

# fruits.remove("apple")
# print(fruits)

# fruits.pop()
# print(fruits) #it will randomly removes value which is at top

fruits.add("apple") # it will print only once 
print(fruits)

# so sets are mostly used when we are storing constants
for fruit in fruits:
    print(fruit)  # it will randomly prints values

print("apple" in fruits)

fruits.pop()
# print(fruits) in sets only

## Tuples
# same as lists but we cant change values

fruits = ("apple", "orange", "banana", "coconut", "orange")
print(fruits)

print(fruits[1]) #it is ordered so it will return index

# fruits[1] = "pineapple"
# print(fruits) # so it will not change the values

print(fruits.index("orange")) #1
print(fruits.count("Apple")) #0

# fruits.add("pineapple")
# print(fruits) so here in tuples no add, remove 

print(fruits) #duplicates ok

print("apple" in fruits)