from time import sleep, time

print("Keep the beat")

target_interval = .5
preview_time = 3

start_time = time()
elapsed_time = 0

while elapsed_time < preview_time:
    print("beat")
    sleep(target_interval)
    elapsed_time = time() - start_time

print("")
print("Now you try")
input("")

capture_time = 3
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

print(f"target interval is {target_interval}")
print("You got")
print(intervals)

sleep(8)
