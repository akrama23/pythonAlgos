various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

# Input: index value (integer)
index = int(input())

# Get the data type of the element at the given index
element = various_data_types[index]
    
# Get the name of the data type using __name__ attribute
data_type = type(element).__name__
    
# Output the result in the specified format
print(f"Element {index}: {data_type}")