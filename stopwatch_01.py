from time import time

input("Test your reaction time")
start_time = time()
input("")
stop_time = time()

elapsed_seconds = stop_time - start_time
elapsed_milliseconds = int(1000 * elapsed_seconds)
print(f"{elapsed_milliseconds} milliseconds")
