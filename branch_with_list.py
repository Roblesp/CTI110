place = {"Colorado", "Washington DC", "Vegas", "Outer Banks"}
wish_list = []
# Get a place from the user
user_input = input("Enter a place you've traveled to: ")

# If statement, have I been to the user's place?
if user_input in place:
    print(f"Yes, I have been to {user_input}")
else:
    print(f"Have not yet been to {user_input}")
    wish_list.append(user_input)

print(f"My travel wish list: {wish_list}")
