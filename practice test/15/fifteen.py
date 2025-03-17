#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")
import pigAge

pig_age = int(input())

converted = pigAge.pigAge_converter(pig_age)

print(f'{pig_age} is {converted} in human years')

