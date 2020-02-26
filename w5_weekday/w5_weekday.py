# Program that returns a
# message based on whether
# it is a weekday or weekend.

days = []

import calendar

for day in calendar.day_name:
    days.append(day)

what_day = input("What day is it? ")

if what_day in days[4:7]:
    print("It is a weekend, yay")
else:
    print("Yes, unfortunately today is a weekday.") 
