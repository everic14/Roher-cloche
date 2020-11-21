from time import localtime, sleep, strftime

while(True):
    time_am_pm = strftime("%I:%M:%S %p", localtime())
    print(time_am_pm, end='\r')
    sleep(1)
