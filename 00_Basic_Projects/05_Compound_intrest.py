# Compound Interest or stocks prices calculator

principle = float(input("Enter principle amount we want to invest: "))
rate = float(input("Enter rate % we need to invest on: "))
time = int(input("Enter how many years you want to invest your money: "))

while principle < 0:
    print(f"Principle value cannot be ${principle}")
    principle = float(input("Enter principle amount we want to invest: "))

while rate < 0:
    print(f"rate value cannot be {rate}%")
    rate = float(input("Enter rate % we need to invest on: "))

while time <= 0:
    print(f"time value cannot be {time} year/s")
    time = int(input("Enter how many years you want to invest your money: "))

total = principle * (pow ((1+rate/100), time))
print(f"Your maturity amount after {time} year/s will be ${total:.2f}.")
