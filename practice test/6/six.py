 # Step 1: Accept the 9-digit student ID number as input
student_id = input()
    
    # Step 2: Split the student ID into three parts and add hyphens
    part1 = student_id[:3]  # First 3 digits
    part2 = student_id[3:5]  # Next 2 digits
    part3 = student_id[5:]  # Last 4 digits
    
    # Step 3: Combine them with hyphens
    formatted_id = part1 + '-' + part2 + '-' + part3
    
    # Step 4: Output the formatted student ID
    print(formatted_id)