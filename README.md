# python-challenge-1
## Module 2 Challenge

The following code examples were used and/or modified to fit this program by prompting the Xpert learning assistant.

# Line 150-163 

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

# Line 195-199

11. Calculate the cost of the order using list comprehension
item_costs = [item['Price'] * item['Quantity'] for item in order_list]
total_cost = sum(item_costs)
print()
print(f"YOUR TOTAL: ${total_cost:.2f}")




