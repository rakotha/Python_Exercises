# Write a Python program to calculate the number of days between two given dates.
from datetime import datetime
date_1 = datetime(2020, 7, 21).date()
date_2 = datetime(2020, 3, 10).date()
print(date_1 - date_2)