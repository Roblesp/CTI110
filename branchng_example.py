# Get the age from the user
age = int(input("Enter your age: "))

# Create a variable called senior
senior = False

# if/else statement
if age >= 65:
    print(f"You are a senior citizen who is {age} years old")

# Boolean is a true or false statement
# -20
# == is equal to 
# != not equal to
    senior = True
elif age < 65 and age >= 18:
    print(f"You are a an adult who is {age} years old")
elif age < 18 and age >= 0:
    print(f"You are a minor who is {age} years old")

# You can not have else without an "if" statement
else: 
    print(f"{age} is not a valid age")    

if senior == True:
    discount = 1.00
else: 
    discount = 0

print(f"At age {age}, your discounts ${discount:.2f}")
