# Iterables -> an object/collection that can return its elements one ata time
# allowing it to be iterated over in loop

#Lists are iterables
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)
#sets are iterables but not reversed

# strings are also iterables
name = "Raj Magdum"
for char in name:
    print(char, end = "  ")