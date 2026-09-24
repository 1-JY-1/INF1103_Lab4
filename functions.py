
def load_inventory(inventory):
    try:
        with open("inventory.txt", "r") as file:

            for line in file:
                data = line.strip().split(",")
                number = int(data[0])
                product_name = data[1]
                quantity = int(data[2])
                print("Once")
                inventory.append([number, product_name, quantity])

    except FileNotFoundError:
        # Create the inventory file
        with open("inventory.txt", "w") as file:
            pass

    return inventory

# def save_inventory(inventory): #, product_name, quantity


#     # starting_number = inventory[-1][0] + 1
#     # inventory.append([starting_number, product_name, quantity])

#     with open("inventory.txt", "w") as file:
#         for item in inventory:
#             file.write(f"{item[0]},{item[1]},{item[2]}\n")


#     return inventory

def get_product_name():

    bcontinue = True

    while bcontinue == True:

        print("Enter the your product name.\n1. Phone\n2. Laptop\n3. Tablet")
        product_name = input("Enter the product name: ")

        if product_name == "Phone" or product_name == "Laptop" or product_name == "Tablet":
            return product_name #get_product_number(product_name)
        else:
            print("Please enter the right product name")
            bcontinue = True
            

    print("Get product Name")

def get_product_quantity(inventory, rejectedEntries, product_name):

    numAmount = False

    while numAmount == False:

        print("===========================================================================")
        amount = input("Enter the number of items to add: ")
        numAmount = amount.isdigit()

        if numAmount == False:

            print("===========================================================================")
            print ("Invalid input. Please enter a valid number.")
            rejectedEntries += 1

        elif numAmount == True:

            if int(amount) < 0:
                print("===========================================================================")
                print("Invalid input. Please enter a positive number.")
                numAmount = False
                rejectedEntries += 1

            else:
                numAmount, inventory, rejectedEntries = process_delivery_amount(numAmount, inventory, int(amount), rejectedEntries, product_name)

                print(numAmount)

                if numAmount == True:
                    return False, int(amount), inventory, rejectedEntries

def get_valid_input(input_prompt, inventory, rejectedEntries):

    total = 0

    for item in inventory:
        total += item[-1]


    if input_prompt.lower() == 'add':


        product_name = get_product_name()
        TF, quantity, inventory, rejectedEntries = get_product_quantity(inventory, rejectedEntries, product_name)

        starting_number = inventory[-1][0] + 1
        inventory.append([starting_number, product_name, quantity])


        # i am here. I need to change the inventory to the list and append the data to the list.
        # So Write a function that change the list and also store the data once it reaches here. (I think have alr)
        # then send this back to the main page and remember to print the inventory nicely, it is not number anymore.
        return TF, inventory, rejectedEntries

                    
    elif input_prompt.lower() == 'calculate tax':

        calculate_tax(total)

        return False, inventory, rejectedEntries
    
    elif input_prompt.lower() == 'quit':
        inventory = save_inventory(inventory)
        generate_report(inventory, rejectedEntries)
        return True, inventory, rejectedEntries
    
    else:
        print("Invalid input. Please try again.")
        return False, inventory, rejectedEntries

def process_delivery_amount(numAmount, inventory, added_value, rejectedEntries, product_name):

    # inventory += added_value

    if added_value > 500:
        added_value -= int(added_value)
        numAmount = False
        rejectedEntries += 1
        print("===========================================================================")
        print(f"Inventory cannot exceed 500 items.\nCurrent Inventory: {added_value}.\nPlease enter a smaller amount.")
        return numAmount, inventory, rejectedEntries

    else:
        print("===========================================================================")
        print("\nNew order Added:")
        print(inventory[-1][0] + 1 , ", " , product_name, ", ", added_value)
        print(f"Added {added_value} items.") #New inventory: {inventory}
        calculate_tax(added_value)
        return numAmount, inventory, rejectedEntries

def calculate_tax(added_value):
    tax_rate = 0.1
    tax_amount = added_value * tax_rate
    print(f"Tax Amount: ${tax_amount:.2f}" )
    return tax_amount

def generate_report(inventory, rejectedEntries):

    final_amount = 0
    # print(inventory)

    for item in inventory:
        final_amount += item[-1]


    print("========== INVENTORY ==========")
    print(f"{'ID':<5}{'Product':<15}{'Quantity':>10}")

    for item in inventory:
        print(f"{item[0]:<5}{item[1]:<15}{item[2]:>10}")
    print("===============================")
    calculate_tax(final_amount)
    print(f"Total rejected entries: {rejectedEntries}")
    print("Exiting the program...")
    print("===========================================================================")








