
is_leap_year = False
   
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,'- leap year')
else:
    print(year,'- not a leap year')