# Import calendar months into list
# and convert list into tuple.

months = []

import calendar
for month in calendar.month_name[1:]:
    months.append(month)

month_tuple = tuple(months)
print(month_tuple)

# Print the summer months from the calendar:
print("\n")
for summer_months in month_tuple[4:7]:
    print(summer_months)
