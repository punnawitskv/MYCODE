from datetime import datetime

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(year):
        days_in_month[2] = 29
    
    day_of_years = sum(days_in_month[:month]) + day
    return day_of_years

def date_diff(date_str1, date_str2):
    date_format = "%d-%m-%Y"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = date2 - date1
    return delta.days

def day_in_year(year):
    return 366 if is_leap(year) else 365

# ตัวอย่างการใช้งาน
day = 1
month = 1
year = 2023

day_of_years = day_of_year(day, month, year)
print(f"Day of year: {day_of_years}")

date_str1 = "1-1-2018"
date_str2 = "1-1-2020"
diff = date_diff(date_str1, date_str2)
print(f"Date difference: {diff} days")

year_for_day_in_year = 2022
days_in_year_result = day_in_year(year_for_day_in_year)
print(f"Days in year {year_for_day_in_year}: {days_in_year_result}")
