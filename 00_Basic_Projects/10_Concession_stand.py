# Concession Stand Program

menu = {"popcorn": 250,
        "samosa": 80,
        "vadapav": 50,
        "icecream": 90,
        "sandwitch": 120}

cart = []
total = 0
food_items = 0

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")

while True:
    food = input("Enter food item/s to buy(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        food_items += 1
    else:
        print("Entered food item is not in list !!")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print( )

print(f"Your total is Rs.{total}")


