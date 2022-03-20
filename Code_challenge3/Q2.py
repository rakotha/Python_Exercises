# Question 2
from datetime import datetime

str_today = datetime.strftime(datetime.today(), "%A %d %B %Y")
print("Today's date is: {}".format(str_today))