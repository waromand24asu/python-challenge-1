# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the Variety Food Truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True

while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    print("--------------------------------------------------")

    # Get the customer's input
    # menu_category = input("Type menu number: ")
    menu_category = input("Please enter menu number you'd like to order from: ")
    print("--------------------------------------------------")
    
    # Check if the customer's input is a number
    if menu_category.isdigit():

        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]

            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")
            print("--------------------------------------------------")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            print("--------------------------------------------------")

            # 2. Ask customer to input menu item number
            menu_selection = input("Enter item # you'd like to order: ")
            print("--------------------------------------------------")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if 1 <= menu_selection <= len(menu_items):
                    selected_item = menu_items[menu_selection]
                    # Store the item name as a variable
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]

                    # Ask the customer for the quantity of the menu item
                    item_quantity = input("Enter quantity (default is 1): ")
                    print("--------------------------------------------------")

                    # Check if the quantity is a number, default to 1 if not
                    if item_quantity.isdigit():
                        item_quantity = int(item_quantity)
                    else:
                        print("Invalid quantity. Defaulting to 1.")
                        item_quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item Name": item_name,
                        "Price": item_price,
                        "Quantity": item_quantity
                    })

                    # Tell the customer that their input isn't valid
                else:
                    print("Invalid input. Please select a valid XX.")
                    print("--------------------------------------------------")

                # Tell the customer they didn't select a menu option
                print("Invalid input. Please select a valid YY.")
                print("--------------------------------------------------")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # while True:
    #     # Ask the customer if they would like to order anything else
    #     keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    # Ask customer if they would like to order anything else.
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
    print("--------------------------------------------------")

    # 5. Check customer input.
    # Take care of exiting loop if customer is finished ordering.
    if keep_ordering.upper() == "N":
        # Exit the ordering question loop.
        place_order = False

    # Show customer their complete order.
    # Loop through the items in the customer's order.
    if order_list and not place_order:  
        print("\n")
        print("Thank you for your order with the Variety Food Truck!")
        print("This is what we are preparing for you.\n")
        print("Item name                 | Price  | Quantity")
        print("--------------------------|--------|----------")

        # Start a loop to iterate through items order, store and display the
        # ordered items, their price and the quantity ordered.
        for item in order_list:
            
            # Store the dictionary items as variables.
            item_name = item["Item Name"]
            item_price = item["Price"]
            item_quantity = item["Quantity"]

            # Calculate the number of spaces for formatted printing.
            num_item_spaces = 25 - len(item_name)
            price_spaces = 5 - len(str(item_price))

            # Create space strings so displayed information is neat.
            item_spaces = " " * num_item_spaces
            price_spaces_str = " " * price_spaces

            # Print the item name, price, and quantity.
            print(f"{item_name}{item_spaces} | ${item_price}{price_spaces_str} | {item_quantity}")

        # Calculate the cost of the order using list comprehension.
        total_price = sum(item["Price"] * item["Quantity"] for item in order_list)
        print("\nTotal Cost: ${:.2f}".format(total_price))

        # Since customer decided to stop, thank them for their order.
        print("\nThank you for visiting with our team at the Variety Food Truck!")

    elif keep_ordering.upper() != "Y":
        # If the order list is empty, prompt the user to try again.
        print("\nYou didn't order anything. Please try again.")
        print("--------------------------------------------------")
        
# Uncomment the following line to check the structure of the order
# print(order_list)

print("Here is your receipt.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
# Provide receipt for customer.
for item in order_list:

    # 7. Store the dictionary items as variables
    item_name = item["Item Name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 25 - len(item_name)
    price_spaces = 5 - len(str(item_price))

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces_str = " " * price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price}{price_spaces_str} | {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
print("\nTotal Cost: ${:.2f}".format(total_cost))
print("\n")
