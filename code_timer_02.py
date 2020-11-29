from time import time


def counting_function(counting_limit):
    for i in range(counting_limit):
        print(i, end="\r")


count_to = 10**5
start_time = time()
counting_function(count_to)
end_time = time()
elapsed = end_time - start_time

print(f"This function took {elapsed} seconds to count to {count_to}")

count_to = 10**6
start_time = time()
counting_function(count_to)
end_time = time()
elapsed = end_time - start_time

print(f"This function took {elapsed} seconds to count to {count_to}")

count_to = 10**7
start_time = time()
counting_function(count_to)
end_time = time()
elapsed = end_time - start_time

print(f"This function took {elapsed} seconds to count to {count_to}")
