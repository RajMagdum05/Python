# ranmdom is a method in python library which gives values randomly
import random
low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "K", "Q", "A"]

print(random.randint(low, high))  # so it will give different no. from 1 to 100 differently each time
print(random.randint(1,6))

print(random.random()) # it will give random floating value btw 0-1

# random choice
print(random.choice(options))

# random shuffle
random.shuffle(cards)
print(cards)