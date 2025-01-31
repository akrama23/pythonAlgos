month = input()
day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December']
        
if month not in months or (day > 31 or day <= 0):
    print('Invalid')
else:
    if month == 'March' and 31 >= day >= 20:
        print('Spring')
    elif month == 'April' or month == 'May':
        print('Spring')
    elif month == 'June' and 20 >= day > 0:
        print('Spring')
    elif month == 'June' and 31 >= day >= 21:
        print('Summer')
    elif month == 'July' or month == 'August':
        print('Summer')
    elif month == 'September' and 21 >= day > 0:
        print('Summer')
    elif month == 'September' and 30 >= day >= 22:
        print('Autumn')
    elif month == 'October' or month == 'November':
        print('Autumn')
    elif month == 'December' and 20 >= day > 0:
        print('Spring')
    elif month == 'December' and 31 >= day >= 21:
        print('Winter')
    elif month == 'January' or month == 'February':
        print('Winter')
    elif month == 'March' and 19 >= day > 0:
        print('Winter')
    else:
        print('Invalid')