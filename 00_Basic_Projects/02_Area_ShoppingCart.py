#1 Area of Rectangle
length = int(input("Enter Length: "))
breadth = int(input("Enter Breadth: "))
print(f"Area of the Rectangle is {length*breadth} cm²")

# cm² -> numlock on + hold Alt + 0178

#2 Shopping Cart
item = input("What you would like to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like to buy: "))

print(f"You had bought {quantity} {item}/s")
print(f"Your total is: Rs. {price*quantity}")