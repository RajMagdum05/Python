# dictionary -> collection of {key:value} pairs
# Oredered and changable.
# No Duplicates allowed

capitals = {"USA": "Washington D. C.",
            "India": "New Delhi",
            "China": "Bejing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA")) # .get to print value of the key

print(capitals.get("Japan")) # it will return none if key is not present in dictionary

if capitals.get("Japan"): # does not exist
    print("That Capitals exists")
else:
    print("Thar capital does not exist")

# To add key value pair and also to update value of the key
capitals.update({"Germany": "Berlin"}) # to add key value pair
capitals.update({"USA": "New York"}) # to update value of key

capitals.pop("China") # it will remove China key value pair
capitals.popitem() # It will remove the latest key value pair i.e. here Germany

#capitals.clear() # to clear dictionary
print(capitals)

#To print keys and values seperately
keys = capitals.keys() # to get only keys
print(keys)

values = capitals.values() # to get only values 
print(values)
# it prints in tupple of lists or list of tuples

for key in capitals.keys(): # capitals.keys() means function having keys in capitals dictionary
    print(key)

for value in capitals.values(): # capitals.keys() and capitals.values() are to get all the keys or values in the dictionary
    print(value) # capitals.get(key name) is to get value for that specific key

# To print key value pair
#items = capitals.items() dont need to write this
for key, value in capitals.items():
    print(f"{key}: {value}")
