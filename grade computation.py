num_grades = int(input("Enter the number of grades (1 to 100): "))
if num_grades < 1 or num_grades > 100:    
    print("Please enter a valid number of grades.")
else:    
    total_grade = 0    
    for i in range(num_grades):        
        grade = float(input(f"Enter grade {i + 1}: "))        
        total_grade += grade    
        average_grade = total_grade / num_grades    
        print(f"Average grade: {average_grade:.2f}")    
        if average_grade >= 50:        
            print("Passed")    
        else:       
            print("Failed")