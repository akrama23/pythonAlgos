#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h
 # Accept the base and height values as inputs
b1 = int(input())
b2 = int(input())
h = int(input())
    
# Calculate the area using the trapezoid area formula
area = ((b1 + b2) / 2) * h
    
# Output the result in the specified format
print(f"Trapezoid area: {area} square meters")