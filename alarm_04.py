import sys
from time import localtime, sleep

if len(sys.argv) != 2:
    print("Set an alarm like this:")
    print(">  python3 alarm_04.py 7:44pm")
    sys.exit()

time_arg = sys.argv[1]

colon_index = time_arg.find(":")

if colon_index == -1:
    print("Set an alarm like this:")
    print(">  python3 alarm_04.py 7:44pm")
    print("Make sure to include a colon")
    sys.exit()

alarm_hour = int(time_arg[:colon_index])

if alarm_hour < 1 or alarm_hour > 12:
    print("Use 12 hour clock time")
    sys.exit()

alarm_minute = int(time_arg[colon_index + 1: colon_index + 3])

if alarm_minute < 0 or alarm_minute > 59:
    print("Minutes need to be between 1 and 59")
    sys.exit()

alarm_am_pm = time_arg[colon_index + 3:]

if len(alarm_am_pm) < 1:
    print("Be sure to include an am/pm in your time")
    sys.exit()

if alarm_am_pm[0] not in ["a", "p"]:
    print("Be sure to include an 'am' or a 'pm' after your time")
    sys.exit()


if alarm_am_pm[0] == "p":
    alarm_hour = alarm_hour + 12

if alarm_am_pm[0] == "a" and alarm_hour == 12:
    alarm_hour = 0

while(True):
    current_hour = localtime().tm_hour
    current_minute = localtime().tm_min

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("beep \a")

    sleep(1)
