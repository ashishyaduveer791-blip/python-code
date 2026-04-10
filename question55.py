# solution  1 uisng date and time modules
# from datetime import datetime

# date = "oct 14 2006  7:15"
# data_time =  datetime.strptime(date, "%b %d %Y %I: %M%p ")
# print(datetime)
# print(type(datetime))

# solution2 using  dateutil module

from dateutil import parser
date_time = parser.parse("Oct 14 2006 7:15Am")
print(date_time)
print(type(date_time))