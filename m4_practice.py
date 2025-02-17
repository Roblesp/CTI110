# In-class practce Module 4 - formatting output

# Get an amount of money from the user
item= input("What item are you purchasing?")
money = float(input("Enter an amount of money with change: "))

# The plus sign is concatentation of string, not additon
print("The amount entered: $" + str(money))
print()
# Usa a formatted string to print a specific amount of places after the decimal 
# little f stands for formating outside the paren.
print(f"The amount entered is ${money:.2f} and the item is{item}")

# This is a formating string
print(f"The amount entered is ${money:.2f} and the item is{item}")

# This is a 