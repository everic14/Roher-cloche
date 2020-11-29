from time import time


def function_to_time():
    for i in range(1_000_000):
        print(i, end="\r")


start_time = time()
function_to_time()
end_time = time()
elapsed = end_time - start_time

print(f"This function took {elapsed} seconds to run")
