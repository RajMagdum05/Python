# 2D Collections - 2D Lists, tuples, sets
# means can store more than 1 1D lists, tuples, sets

fruits = ["apple", "orange", "banana", "coconut"] # -> row 1
vegetables = ["tomato", "onion", "potato", "pepper"] # -> row 2
proteins = ["paneer", "tofu", "eggs", "chicken"] # -> row 3

foods = [fruits, vegetables, proteins]
# foods = [["apple", "orange", "banana", "coconut"], ["tomato", "onion", "potato", "pepper"], ["paneer", "tofu", "eggs", "chicken"]]

print(foods[0]) #prints row 1 entire

#              col 1   col 2   col 3   col 4
#       index    0      1        2       3
# row 1   0 -> apple   orange  banana  coconut
# row 2   1 -> tomato  onion   potato  pepper
# row 3   2 -> paneer  tofu    eggs    chicken

print(foods[0][1]) #orange first[] -> row, second[] -> column

# foods[0][0] = "pineapple"
# print(foods)  # we can change

for collection in foods:
    for food in collection:
        print(food, end=" ") # so it will print all values first from row 1 then row 2 and then row 3
    print()
#so food means it will print entire row at once

# so this can be true for tuples and sets also
# foods = [(),(),()] or foods = ({},{}{})
