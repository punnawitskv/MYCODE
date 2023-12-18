day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
  if is_leap(year):
      day_in_month[2] = 29
  if month < 1 or month > 12 or day < 1 or day > day_in_month[month]:
      return "Invalid date"
  day_of_year = sum(day_in_month[:month]) + day
  return day_of_year

def day_in_year(year):
  return 366 if is_leap(year) else 365

def date_diff(date1, date2):
  day1, month1, year1 = map(int, date1.split('-'))
  day2, month2, year2 = map(int, date2.split('-'))

  if (
      day1 > 0 and day1 < 32 and month1 > 0 and month1 < 13 and year1 > 0 and
      day2 > 0 and day2 < 32 and month2 > 0 and month2 < 13 and year2 >= year1
  ):
      if(year2-year1 <= 1):
        total_days_difference = 1
      else:
        total_days_difference = 0
      for year in range(year1+1, year2):
          total_days_difference += day_in_year(year)
      sumyear1 = day_in_year(year1) - day_of_year(day1,month1,year1)
      total_days_difference += day_of_year(day2, month2, year2) + sumyear1

      return (total_days_difference+1)
  else:
      return ("Invalid date input")

# first_date = input("Enter the first date (dd-mm-yyyy): ")
# secound_date = input("Enter the second date (dd-mm-yyyy): ")

# date_diff(first_date, secound_date)
#print(date_diff("25-12-1999", "9-3-2000"))