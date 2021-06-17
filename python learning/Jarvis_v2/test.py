from datetime import datetime
from time import time

time_str = '3 p.m.'
time_str = time_str.replace(".", "")
print(time_str.upper())


datetime_object = time.strftime(time_str, '%I %p')
time_now = datetime.now()
print(datetime_object)
print(time_now)