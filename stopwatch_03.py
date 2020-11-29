from time import time

print("Repeat yourself")
input("Hit enter, count three Mississippi's, then hit it again")
start_time = time()
input("")
stop_time = time()

elapsed_first_try = stop_time - start_time

input("Now do it again with the same timing")
start_time = time()
input("")
stop_time = time()

elapsed_second_try = stop_time - start_time

elapsed_difference = elapsed_second_try - elapsed_first_try

messages = [
    "The second time was way faster",
    "The second time was clearly faster",
    "The second time was a little faster",
    "The second time was a tiny bit faster",
    "Almost exactly!",
    "The second time was a tiny bit slower",
    "The second time was a little slower",
    "The second time was clearly slower",
    "The second time was way slower",
]

if elapsed_difference < -.600:
    print(messages[0])
elif elapsed_difference < -.300:
    print(messages[1])
elif elapsed_difference < -.100:
    print(messages[2])
elif elapsed_difference < -.030:
    print(messages[3])
elif elapsed_difference < .030:
    print(messages[4])
elif elapsed_difference < .100:
    print(messages[5])
elif elapsed_difference < .300:
    print(messages[6])
elif elapsed_difference < .600:
    print(messages[7])
else:
    print(messages[8])

print(f"    {int(1000 * elapsed_difference)} milliseconds")
