#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")
import pigAge

# Taking integer input
pig_age = int(input())

# Converting pig age to human years using the given function
human_age = pigAge.pigAge_converter(pig_age)

# Printing the result in the required format
print(f"{pig_age} is {human_age} in human years")

