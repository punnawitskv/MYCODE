def is_leap(year):
  return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day,month,year):
  day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
  day_of_year = 0
  if is_leap(year) :
      day_in_month[2] += 1
  else:
      if month == 2 and day == 29:
          return -1
  for i in range(1,month):
      day_of_year += day_in_month[i]
  day_of_year += day 

  return day_of_year

def day_in_year(year):
  day = 365
  if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
      day = 366
  return day

def date_diff(date1: str, date2: str):
  date1 = list(map(int, date1.split('-')))
  date2 = list(map(int, date2.split('-')))

  if date1[2] == date2[2]:
      dates = day_of_year(date2[0], date2[1], date2[2]) - day_of_year(date1[0], date1[1], date1[2]) + 1
  else:
      dates = day_in_year(date1[2]) - day_of_year(date1[0], date1[1], date1[2]) + day_of_year(date2[0], date2[1], date2[2]) + 1

  if date2[2] - date1[2] > 1:
      for year in range(date1[2] + 1, date2[2]):
          dates += day_in_year(year)

  return dates

print(date_diff("25-12-1999", "9-3-2000"))