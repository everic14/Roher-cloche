from subprocess import call
from time import time

start_time = time()
command_to_time = "python3 timer_05.py 13"
call(command_to_time, shell=True)
end_time = time()
elapsed = end_time - start_time

print(f"This command took {elapsed} seconds to run")
