num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

''' Your solution goes here '''
# for loop in nums_row starting at 1 not 0
for row in range(1, num_rows + 1):  
    for col in range(num_cols):
        # str(row) convert row to string
        #65 = 'A' -- chr converts 65 + col to letter
        seat = str(row) + chr(65 + col)
        print(seat, end=' ')
print()


# Testing with inputs: 2 3
# Your output
# 1A 1B 1C 2A 2B 2C 
# Testing with inputs: 5 3
# Your output
# 1A 1B 1C 2A 2B 2C 3A 3B 3C 4A 4B 4C 5A 5B 5C 
# Testing with inputs: 5 0
# Your output

# Testing with inputs: 0 2
# Your output
