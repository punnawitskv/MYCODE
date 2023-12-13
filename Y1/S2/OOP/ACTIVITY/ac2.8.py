from datetime import datetime

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def date_diff(date_str1, date_str2):
    date_format = "%d %m %Y"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)

    days_difference = abs((date2 - date1).days)
    return days_difference

def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365

date_str1 = input("Enter the first date (dd mm yyyy): ")
date_str2 = input("Enter the second date (dd mm yyyy): ")

diff_result = date_diff(date_str1, date_str2) + 1
print(f"Date difference between {date_str1} and {date_str2} is: {diff_result} days")