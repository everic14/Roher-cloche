from time import time

input("Test your reaction time")
start_time = time()
input("")
stop_time = time()

elapsed_seconds = stop_time - start_time
elapsed_milliseconds = int(1000 * elapsed_seconds)
print(f"{elapsed_milliseconds} milliseconds")

if elapsed_milliseconds < 100:
    print("Super fast!")
elif elapsed_milliseconds < 200:
    print("Pretty quick")
elif elapsed_milliseconds < 400:
    print("Keep trying")
elif elapsed_milliseconds < 800:
    print("Slooooow")
else:
    print("Are you awake?")

