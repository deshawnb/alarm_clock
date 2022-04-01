import datetime
from alarm_clock import Alarm_Clock


alarm_time = datetime.time(12, 12, 12)
is_alarm_on = True
clock_time = Alarm_Clock(alarm_time,is_alarm_on)
clock_time.tell_time()
print(alarm_time)



# x = datetime.datetime.now()

# print(x.strftime("%X"))
