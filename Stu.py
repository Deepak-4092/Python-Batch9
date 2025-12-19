# List of students as (FirstName, Surname)
students = [
    ("Rohit", "Sharma"), 
    ("Rahul", "Gupta"), 
    ("Anita", "Patel"), 
    ("Ravi", "Bishnoi"), 
    ("Virat", "Kohli"),
    ("Sunil", "Rao"), 
    ("Ravi", "Ashwin"), 
    ("Venkatesh", "Iyer"),
    ("Deepak", "Verma"), 
    ("Arjun", "Malhotra"), 
]

for i in range(0, len(students), 2):
    left = f"{students[i][0]}, {students[i][1]}"
    right = f"{students[i+1][0]}, {students[i+1][1]}"
    print(f"{left:<20} {right}")


# Dictionary to track first names and surnames
name_dict = {}
duplicates = {}

for first, last in students:
    if first in name_dict:
        # If surname is different, store only one duplicate
        if name_dict[first] != last:
            duplicates[first] = (name_dict[first], last)
    else:
        name_dict[first] = last

# Display result
print("Students with same name but different surname:")
for name, surnames in duplicates.items():
    print(f"{name}: {surnames[0]} , {surnames[1]}")