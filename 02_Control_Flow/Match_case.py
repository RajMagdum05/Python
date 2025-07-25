## Match Case -> switch case statement
# Alternative to many if-else statemnt

# x = [1, 2, 3]
# y=x
# y.append(4)
# print(x)

# so here y=x means it does not create new list
# it creates new reference to the same list as x
# so y.append(4) means it modifies list that both x and y refer to

def is_day(day):
    match day:
        case 1: 
            return "Sunday"
        case 2: 
            return "Monday"
        case 3: 
            return "Tuesday"
        case 4: 
            return "Wednesday"
        case 5: 
            return "Thursday"
        case 6: 
            return "Friday"
        case 7: 
            return "Saturday"
        case _: 
            return "Not a valid day!!" 
print(is_day(1))

day = input("Enter a day: ").lower()
match day:
    case "sunday":
        print("Weekend")
    case "saturday":
        print("Weekend")
    case "monday":
        print("Week day")
    case "tuesday":
        print("Week day")
    case "wednesday":
        print("Week day")
    case "thursday":
        print("Week day")
    case "friday":
        print("Week day")
    case _:
        print("Invalid day!!")

# or we can dp this to it
day = input("Enter a day: ").lower()
match day:
    case "sunday" | "saturday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Week day")

    