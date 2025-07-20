# Logical operators -> Evaluate mutiple conditions
# or - at least one condition should be True
# and - all conditions should be true
# not - inverts the condition  True -> False and False->True

# in python its words like and, or, not and not &&,||,!

temp = 290
is_sunny = False

if temp >= 28 and is_sunny:
    print("Its hot outside")
elif temp < 28 and temp > 0 and is_sunny:
    print("It's Warm outside")
elif temp < 0 and is_sunny:
    print("Its cold and sunny")
elif temp >= 28 and not is_sunny:
    print("Its hot outside")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It's Warm outside")
elif temp < 0 and not is_sunny:
    print("Its cold and sunny")
else:
    print("Enter Correct Temp!!")

# Validate user input exercise
# 1) Username is no more than 12 characters
# 2) Username must not contain spaces
# 3) Username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username should not have more than 12 characters.")
elif username.find(" ") != -1:
    print("Your username should not contain spaces.")
elif not username.isdigit():
    print("Your username should not contain digits.")
else:
    print(f"Hello {username}")