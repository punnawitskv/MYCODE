def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days_in_month[2] = 29

    if month < 1 or month > 12 or day < 1 or day > days_in_month[month]:
        return "Invalid date"

    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year

day, month, year = map(int, input("Enter the date (dd mm yyyy): ").split())

day_result = day_of_year(day, month, year)

print(f"The day of the year is: {day_result}")
#print("The day of the year is:" ,day_result)