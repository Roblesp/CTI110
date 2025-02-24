# Perla Robles
# 02/24/2025
# P2HW2
# Use list to capture students grades

# Get 6 grades from the user -they should be floats
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Create an empty list
grades_list = []

# Use the append method to add all grades into the list 
# Code look like this: list_name.append(what_to_add_to_list)

grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
grades_list.append(grade6)

# Display the list
print(grades_list)
print()

# Display vales to user
print("-----------Reults----------")
print(f"{'Lowest Grade:':<20} {min(grades_list)}")
print(f"{'Highest Grade:':<20} {max(grades_list)}")
print(f"{'Highest Grade:':<20} {sum(grades_list)}")
average = sum(grades_list) / len(grades_list)
print(f"{'Average:':<20} {average:.2f}")
print("---------------------------------")