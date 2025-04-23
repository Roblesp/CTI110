# Create outer loop that runs until user inputs "Done"

# Create the accumulator variables
total_subtotal = 0
total_tax = 0
grand_total_tax = 0

item_name = input("Enter item name or 'Done' to terminate: ")
while item_name.lower() != "done":
    #print(f"Loop is running bc you put in {item_name}")
    # In hw, below, ask for hours_worked and pay_rate
    quantity = int(input(f"How many {item_name} will you buy? "))
    price = float(input(f"How much does {item_name} cost? "))

    # Code to caluclate the values
    total_item_cost = quantity * price
    tax = total_item_cost * 0.06
    total_with_tax = total_item_cost + tax

    # Add to the accumulator variables
    total_subtotal += total_item_cost
    total_tax += tax
    grand_total_tax += total_with_tax

    # In hw, this is your print statements
    print(f"Subtotal: ${total_item_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total with Tax: ${total_with_tax:.2f}")

    item_name = input("Enter item name or 'Done' to terminate: ")
# Loop has broken, display final accumulated totals below
print()
print()
print(f"The total for all items BEFORE tax is ${total_subtotal:.2f}")
print(f"The total tax on all items is ${total_tax:.2f}")
print(f"The total for all items including tax is ${grand_total_tax:.2f}")


