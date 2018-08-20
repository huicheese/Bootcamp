def minutes_to_years_days(minutes):
    days = minutes/(60*24)
    years = days/365
    days = days%365
    return years, days
Minutes = input('Enter the number of minutes:')
a,b=minutes_to_years_days(500)
print(a)
print(b)