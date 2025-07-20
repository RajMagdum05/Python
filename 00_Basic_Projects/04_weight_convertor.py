# Weight Convertor Program
weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds (K or L): ").lower()

if unit == "k":
    print(f"Your Weight is {weight*2.205} Lbs.")
elif unit == "l":
    print(f"Your Weight is {weight/2.205} Kgs.")
else:
    print(f"{unit} is not valid!!")
