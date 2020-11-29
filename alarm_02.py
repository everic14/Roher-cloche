import sys
from time import localtime, sleep

time_arg = sys.argv[1]
colon_index = time_arg.find(":")
alarm_hour = int(time_arg[:colon_index])
alarm_minute = int(time_arg[colon_index + 1:])

while(True):
    current_hour = localtime().tm_hour
    current_minute = localtime().tm_min

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("beep \a")

    sleep(1)
