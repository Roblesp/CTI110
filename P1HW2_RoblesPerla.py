 # Perla Robles
 # 2/12/2025
 # P1HW2
 # A brief description of the project

print("This program calculates and displays travel expenses ")
print()
budget = int(input("Enter Budget: "))
print()
destination = input("Enter you travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
remaining_balance = budget - (gas + hotel + food)
print()

print("-------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food:", food)
print()
print("Remaining Balance: ", remaining_balance)


