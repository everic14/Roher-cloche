import sys
from time import sleep

seconds_left = float(sys.argv[1])
interval = .01

done = False
while(not done):
    sleep(interval)
    print(f"{seconds_left:0.3f}   ", end="\r")
    seconds_left = seconds_left - interval
    if seconds_left <= 0:
        done = True

print("ding     ")
