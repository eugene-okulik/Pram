from datetime import datetime

time_str = "Jan 15, 2023 - 12:05:33"

date_time = datetime.strptime(time_str, "%b %d, %Y - %H:%M:%S")
print(date_time.strftime("%B"))
print(date_time.strftime("%d:%m:%Y, %H:%M"))
