import datetime
import datetime
class Alarm_Clock:
    def __init__(self, alarm_time, is_alarm_on):
        self.current_time = datetime.datetime.now()
        self.alarm_time = alarm_time
        self.is_alarm_on = is_alarm_on

    def tell_time(self):
        print(self.current_time.strftime("%X"))