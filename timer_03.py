from time import sleep

seconds_left = 11

done = False
while(not done):
    sleep(1)
    print(f"{seconds_left}   ", end="\r")
    seconds_left = seconds_left - 1
    if seconds_left <= 0:
        done = True

print("ding")
