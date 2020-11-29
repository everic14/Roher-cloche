from time import time


def counting_function(counting_limit):
    for i in range(counting_limit):
        print(i, end="\r")


def function_timer(function_to_time, count_to):
    start_time = time()
    function_to_time(count_to)
    end_time = time()
    elapsed = end_time - start_time
    return elapsed


count_to = 10**5
elapsed = function_timer(counting_function, count_to)
print(f"This function took {elapsed} seconds to count to {count_to}")

count_to = 10**6
elapsed = function_timer(counting_function, count_to)
print(f"This function took {elapsed} seconds to count to {count_to}")

count_to = 10**7
elapsed = function_timer(counting_function, count_to)
print(f"This function took {elapsed} seconds to count to {count_to}")
