class AlarmClock:
    def __init__(self):
        self.current_time = ''
        self.alarm_time = ''
        self.is_alarm_on = False

    def set_time(self):
        user_input = str(input('set the time.'))
        self.current_time = user_input
        print(f'the time is now {user_input}.')
        return

    def set_clock_alarm(self):
        user_input = input('press y or n to turn on alarm: ')
        if user_input == 'y':
            print('the alarm is on now!')
            self.is_alarm_on = True
        elif user_input == 'n':
            print('the alarm is off.')
            self.is_alarm_on = False
        else:
            print('invalid input')
        return

    def set_alarm_time(self):
        if self.is_alarm_on == True:
            user_input = str(input('set the alarm time.'))
            self.alarm_time = user_input
            print(f'the alarm time is now {user_input}.')
        else:
            print('alarm not set')
        return

    def clock_result(self):
        if self.is_alarm_on == True:
            print(f'the time is {self.current_time} you have set the alarm to {self.alarm_time}')
        else:
            print(f'you have set the time to {self.current_time}, the alarm is off')

