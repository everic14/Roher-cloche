from time import sleep

interval = .001
seconds_left = 11

done = False
while(not done):
    sleep(interval)
    print(f"{seconds_left:0.3f}   ", end="\r")
    seconds_left = seconds_left - interval
    if seconds_left <= 0:
        done = True

print("ding     ")
