import functions


toQuit = False
rejectedEntries = 0
current_inventory = 0
inventory = []
inventory = functions.load_inventory(inventory)



print("===========================================================================")
print("Welcome to the Smart Inventory Auditor!")
print("You can add items to the inventory or quit the program.")
print("The maximum inventory limit is 500 items.")

# current inventory is {current_inventory}

# print("===========================================================================")

while toQuit == False:

    print("===========================================================================")
    print("Enter 'add' to add items, 'calculate tax' to calculate tax, or 'quit' to exit.")
    # print(f"Current inventory: {current_inventory}")

    user_input = input("Your choice: ")

    toQuit, inventory, rejectedEntries = functions.get_valid_input(user_input, inventory, rejectedEntries)

    # print("Toquit:", toQuit)
    # print("Inventory:", current_inventory)
    # print("Rejected Entries:", rejectedEntries)


