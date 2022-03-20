# Question 4
from datetime import datetime,timedelta
str_Yesterday = datetime.strftime(datetime.today()-timedelta(days=1),"%Y-%m-%d")
str_today = datetime.strftime(datetime.today(), "%Y-%m-%d")
str_tomorrow = datetime.strftime(datetime.today()+timedelta(days=1),"%Y-%m-%d")
print("Yesterday: {}".format(str_Yesterday))
print("Today: {}".format(str_today))
print("Tomorrow: {}".format(str_tomorrow))