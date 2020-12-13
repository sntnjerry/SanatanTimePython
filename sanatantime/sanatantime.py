'''

Welcome to Sanatan Time!

Python module that converts the 
currently used christian system 
time to the historic and vedic
sanatan system time.

All the conversion formulas and 
explanation of the conversion system
can be found in the "readme.md" file
present with this file.

To use this module, simply install
using pip (pip install sanatantime).

For guidance regarding the module,
kindly read the "readme.md" file present with this
file.

Jai Shree Ram!

'''

import datetime

class SanatanTime:
    
    def __init__(self, sanatan_time_start = [3, 30]):
        if sanatan_time_start[0] > 23 or sanatan_time_start[1] > 59:
            return "Invalid Sun Rise (Day Start) Time."
        self.sanatan_time_start = sanatan_time_start
        christian_current_time = datetime.datetime.now()
        milliseconds = christian_current_time.microsecond // 1000
        seconds = christian_current_time.second + (milliseconds / 1000)
        sanatan_converted_time = self.christian_to_sanatan_time(christian_current_time.hour, christian_current_time.minute, seconds)
        self.ghadi = sanatan_converted_time[0]
        self.pal = sanatan_converted_time[1]
        self.lipt = sanatan_converted_time[2]
        self.vilipt = sanatan_converted_time[3]
        self.current_sanatan_time = str(self.ghadi) + " Ghadis, " + str(self.pal) + " Pals, " + str(self.lipt) + " Lipts, " + str(self.vilipt) + " Vilipts"
    
    def hours_difference(self, start_hour, end_hour):
        if end_hour >= start_hour:
            return end_hour - start_hour
        else:
            return 24 - (start_hour - end_hour)
    
    def christian_to_sanatan_time(self, hours, minutes, seconds):
        minutes_from_day_start = 0
        if hours == self.sanatan_time_start[0] and minutes >= self.sanatan_time_start[1]:
            minutes_from_day_start = minutes - self.sanatan_time_start[1]
        else:
            minutes_from_day_start = (60 - self.sanatan_time_start[1]) + (self.hours_difference(self.sanatan_time_start[0] + 1, hours) * 60) + minutes
        ghadis = int(minutes_from_day_start / 24)
        minutes_from_ghadi_start = minutes_from_day_start % 24
        pals = int(((minutes_from_ghadi_start * 60) + seconds) / 24)
        lipts = int((((minutes_from_ghadi_start * 60) + seconds) % 24) / 0.4)
        vilipts = int(((((minutes_from_ghadi_start * 60) + seconds) % 24) % 0.4) * 150)
        return [ghadis, pals, lipts, vilipts]
    
    def convert(self, christian_time):
        milliseconds = christian_time.microsecond // 1000
        seconds = christian_time.second + (milliseconds / 1000)
        sanatan_converted_time = self.christian_to_sanatan_time(christian_time.hour, christian_time.minute, seconds)
        return str(sanatan_converted_time[0]) + " Ghadis, " + str(sanatan_converted_time[1]) + " Pals, " + str(sanatan_converted_time[2]) + " Lipts, " + str(sanatan_converted_time[3]) + " Vilipts"
    
    def now(self):
        return self.current_sanatan_time
