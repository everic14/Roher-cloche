import sys
from time import localtime, sleep

alarm_hour = int(sys.argv[1])
alarm_minute = int(sys.argv[2])

while(True):
    current_hour = localtime().tm_hour
    current_minute = localtime().tm_min

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("beep \a")

    sleep(1)
