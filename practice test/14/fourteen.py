#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100

import math 

# Taking integer input
num = int(input())

# Calculating factorial
factorial_value = math.factorial(num)

# Checking if factorial is greater than 100
is_greater_than_100 = factorial_value > 100

# Printing results
print(factorial_value)
print(is_greater_than_100)