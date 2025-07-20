#Contdown Timer in python - to wait for some sec to print 
# python have function import time and time.sleep(1) for suppose 1 sec

import time
my_time = int(input("Enter your time in seconds: "))

for x in range(my_time, 0, -1): #to print it reverse we can also do this
    seconds = x%60
    minutes = int(x/60)%60 # for sec > 3600 min should increase than 59 
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)