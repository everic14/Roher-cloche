from time import sleep, time
import numpy as np

print("Keep the beat")

target_interval = .4
preview_time = 4

start_time = time()
elapsed_time = 0

while elapsed_time < preview_time:
    print("beat")
    sleep(target_interval)
    elapsed_time = time() - start_time

print("")
print("Now you try")
input("")

capture_time = 4
start_time = time()
last_time = start_time
elapsed_time = 0
intervals = []
while elapsed_time < capture_time:
    print("beat", end="\r")
    input("")
    this_time = time()
    elapsed_time = this_time - start_time
    interval = this_time - last_time
    intervals.append(interval)
    last_time = this_time

interval_array = np.array(intervals)
errors = interval_array - target_interval
absolute_errors = np.abs(errors)
mean_absolute_error = np.mean(absolute_errors)
scaled_mae = mean_absolute_error / target_interval

thresholds = [.1, .2, .3, .5]
messages = [
    "Rock solid timing",
    "Pretty steady",
    "Close-ish",
    "Don't quit your day job",
    "You have no rhythm",
]

if scaled_mae < thresholds[0]:
    print(messages[0])
elif scaled_mae < thresholds[1]:
    print(messages[1])
elif scaled_mae < thresholds[2]:
    print(messages[2])
elif scaled_mae < thresholds[3]:
    print(messages[3])
elif scaled_mae < thresholds[4]:
    print(messages[4])
else:
    print(messages[5])

sleep(8)
