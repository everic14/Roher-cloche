import time

while(True):
    date_and_time = time.ctime()
    time_only = date_and_time[11:20]
    print(time_only, end='\r')
    time.sleep(1)
