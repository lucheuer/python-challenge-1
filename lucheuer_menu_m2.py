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
print("-------------------------------------")
print("Welcome to Chef Luc's Food Truck.")
print("-------------------------------------")

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

    # Get the customer's input
    menu_category = input("Type Menu Number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

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
                        num_item_spaces = 24 - len(key + " - " + key2)
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
            # 2. Ask customer to input menu item number
            selection_number = input("Please enter your selection: ")

            # 3. Check if the customer typed a number
            if selection_number.isdigit():
                # Convert the menu selection to an integer
                selection_number = int(selection_number)

                # 4. Check if the menu selection is in the menu items
                if selection_number in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[selection_number]["Item name"]
                    # Store the item price as a variable
                    item_price = menu_items[selection_number]["Price"]
                    # Ask the customer for the quantity of the menu item
                    selection_quantity = input(f"How many {item_name}s would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if not selection_quantity.isdigit():
                        print("Invalid Input. Defaulting quantity to 1. ")
                        selection_quantity = 1
                    else:
                        selection_quantity = int(selection_quantity)

                    # Add the item name, price, and quantity to the order list
                    order_list.append({"Item name": item_name, "Price": item_price, "Quantity": selection_quantity})

                    # Print current order
                    print("\nCurrent order:")
                    print("----------------")
                    for order in order_list:
                        print(f"{order['Item name']} : {order['Quantity']} @ ${order['Price']} each")

                else:
                    print(f"Selection number {selection_number} is not valid.")
            else:
                print(f"{selection_number} is not a valid number.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print(f"{menu_category} is not a valid number.") 

    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? Please enter (Y) for Yes or (N) for No: ")
    if keep_ordering.upper() != "Y":
        place_order = False
        print("-----------------------------")
        print("Thank you for your order. :) ")
        print("-----------------------------")

# Print out the customer's order
print("----------------------------------------")
print("Here is your order, Coming right up!: ")
print("----------------------------------------")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order in order_list:
    # 7. Store the dictionary items as variables
    item_name = order['Item name']
    price = order['Price']
    quantity = order['Quantity']

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    item_spaces = " " * num_item_spaces

    # 9. Create space strings and print the item name, price, and quantity
    print(f"{item_name}{item_spaces}  | ${price:.2f} | {quantity}")

# 11. Calculate the cost of the order using list comprehension
item_costs = [item['Price'] * item['Quantity'] for item in order_list]
total_cost = sum(item_costs)
print()
print(f"YOUR TOTAL: ${total_cost:.2f}")