#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

# Input the number of ounces
ounces = int(input())
    
# Calculate tons, pounds, and ounces
tons = ounces // 32000  # 1 ton = 32,000 ounces (16 ounces/pound * 2000 pounds/ton)
ounces_remaining = ounces % 32000
    
pounds = ounces_remaining // 16  # 1 pound = 16 ounces
ounces_remaining = ounces_remaining % 16

# Output the result
print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces_remaining}")