from time import sleep, time

duration = 2
number_of_hits = 0
elapsed_time = 0
input("Hit enter as many times as you can in two seconds")
start_time = time()

while elapsed_time < duration:
    number_of_hits += 1
    input("")
    elapsed_time = time() - start_time

thresholds = [2, 4, 8, 12, 16]
messages = [
    "Try again",
    "Sloth",
    "Turtle",
    "Rabbit",
    "Horse",
    "Cheetah",
]

print(f"{number_of_hits} hits")
if number_of_hits < thresholds[0]:
    print(messages[0])
elif number_of_hits < thresholds[1]:
    print(messages[1])
elif number_of_hits < thresholds[2]:
    print(messages[2])
elif number_of_hits < thresholds[3]:
    print(messages[3])
elif number_of_hits < thresholds[4]:
    print(messages[4])
else:
    print(messages[5])

sleep(3)
