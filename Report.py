# Read student name
student_name = input("Enter student name: ")

# Read marks of 5 subjects
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 = int(input("Enter marks for Subject 5: "))

# Function to calculate result
def student_result(name, s1, s2, s3, s4, s5):
    # Calculate total marks
    total = s1 + s2 + s3 + s4 + s5
    
    # Calculate percentage
    percentage = total / 5
    
    # Display student details
    print("\nStudent Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    
    # Check pass or fail condition
    if percentage >= 60:
        print("Result: Pass")
    else:
        print("Result: Fail")

# Call the function
student_result(student_name, sub1, sub2, sub3, sub4, sub5)
