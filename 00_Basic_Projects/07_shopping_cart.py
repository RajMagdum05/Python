# Shopping Cart Program

foods = []
prices = []

while True:
    food = input("Enter the food you like to order (q to quit): ").lower()
    if(food == "q"):
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

# print("----Your Cart----")
# print()
# for food in foods:
#     print(food)

# print()
# total = 0
# for price in prices:
#     total += price

# print(f"Your total is: ${total:.2f}")

print("\n----- Your Cart -----\n")
print()
print(f"{"Food":15} {"Price":>8}")
print("-"*26)

total = 0

for food,price in zip(foods, prices): # To print both lists at a time make it as a zip 
    print(f"{food:15} ${price:>5.2f}")
    total += price

print("-"*26)
print(f"{"Total":15} ${total:>6.2f}")
