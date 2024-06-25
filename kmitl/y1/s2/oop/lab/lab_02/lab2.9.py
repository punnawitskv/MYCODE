def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[2] = 29
    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year

def total_days_in_years(start_year, end_year):
    total_days = 0
    for year in range(start_year, end_year + 1):
        total_days += 366 if is_leap(year) else 365
    return total_days

def date_diff(day1, month1, year1, day2, month2, year2):
    day_result1 = day_of_year(day1, month1, year1)
    day_result2 = day_of_year(day2, month2, year2)
    days_in_full_years = total_days_in_years(year1 + 1, year2 - 1)
    if year2 > year1:
        total_days_difference = days_in_full_years + day_result2 + (365 - day_result1)
    else:
        total_days_difference = days_in_full_years + day_result2 - day_result1
    return total_days_difference

day1, month1, year1 = map(int, input("Enter the first date (dd mm yyyy): ").split())
day2, month2, year2 = map(int, input("Enter the second date (dd mm yyyy): ").split())

if day1>0 and day1<32 and month1>0 and month1<13 and year1 > 0 and day2>0 and day2<32 and month2>0 and month2<13 and year2>=year1:
    total_days_differenc = date_diff(day1, month1, year1, day2, month2, year2) + 1
    print(f"The number of days between {day1}/{month1}/{year1} and {day2}/{month2}/{year2} is: {total_days_differenc} days")
else:
    print("Brrrrrr(-1)")