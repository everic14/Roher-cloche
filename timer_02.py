from time import sleep

seconds_left = 15
for i_second in range(seconds_left):
    print(f"{seconds_left - i_second}   ", end="\r")
    sleep(1)

print("ding")
