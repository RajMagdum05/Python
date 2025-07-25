# List comprehension = A concise way to create list in python
# Compact and easier to read 
# [expresssion for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x*2)
print(doubles)

# so instead of these all statement we can write ->
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

triples = [x * 3 for x in range(1, 11)]
print(triples)

squares = [x * x for x in range(1, 11)]
print(squares)

## For List
fruits = ["Apple", "Banana", "Gauva", "pineapple"]
# fruit = [fruit.upper() for fruit in fruits]
# print(fruit)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

### If Condition used here
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive = [num for num in numbers if num>=0]
negative = [num for num in numbers if num<0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print(positive)
print(negative)
print(even)
print(odd)

# 
grades = [85, 42, 79, 90, 56, 61, 30]
passing = [grade for grade in grades if grade >= 60]
print(passing)