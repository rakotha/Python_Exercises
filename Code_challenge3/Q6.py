# Question 6
from datetime import timedelta
stime = 996452
strTimeorg = str(timedelta(seconds = stime))
strTime = strTimeorg.split(':')
print('Days : Hours : Minutes : Seconds -> {} : {} : {} : {}'.format(strTime[0][:2], strTime[0][9:11], strTime[1], strTime[2]))
