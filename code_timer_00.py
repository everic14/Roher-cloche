from time import time

start_time = time()

for i in range(1_000_000):
    print(i, end="\r")

end_time = time()
elapsed = end_time - start_time

print(f"This code took {elapsed} seconds to run")
