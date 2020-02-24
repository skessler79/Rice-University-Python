"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    date1 = datetime.date(year, month, 1)
    date2 = datetime.date(year, month, 1)
    if(month == 12):
        date2 = datetime.date(year + 1, 1, 1)
    else:
        date2 = datetime.date(year, month + 1, 1)
    diff = date2 - date1
    
    return diff.days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    valid = True
    
    if (year < datetime.MINYEAR):
        #nonlocal valid
        valid = False
    if (year > datetime.MAXYEAR):
        #nonlocal valid
        valid = False
    if (month < 1):
        #nonlocal valid
        valid = False
    if (month > 12):
        #nonlocal valid
        valid = False
    if not(valid):
        return valid
    if (day > days_in_month(year, month)):
        #nonlocal valid
        valid = False
    if day < 1:
        #nonlocal valid
        valid = False
    return valid

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if not(is_valid_date(year1, month1, day1)):
        return 0
    if not(is_valid_date(year2, month2, day2)):
        return 0
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    diff = date2 - date1
    if(diff.days < 0):
        return 0
    return diff.days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    if not(is_valid_date(year, month, day)):
        return 0
    today = datetime.date.today()
    date1 = datetime.date(year, month, day)
    diff = today - date1
    
    if(diff.days < 0):
        return 0
    
    return diff.days

#print(days_in_month(2020, 2))
print(is_valid_date(1992428, 12, 20))
#print(days_between(2015, 12, 23, 2018, 5, 15))
#print(age_in_days(1996, 7, 30))
