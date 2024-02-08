#---------------------------------------------------------------------------------------------------#
# This is a pet shop program
# A user can see a list of products, add products, delete products, checkout
# the inventory list of products is scalable and allows to add new items or delete
# A user can add custom product and choose quantity
# A user can delete any product in the cart and choose quantity
# the program shows calculations of item quantity and their prices
# the program handle unexpected inputs and shows error messages
# added user-friendly interface for better user experience
#---------------------------------------------------------------------------------------------------#
from datetime import datetime

inventory = {
    1: {'name': 'Wiskers Cat Food', 'price': 2.99, 'quantity': 0},
    2: {'name': 'Kong', 'price': 3.45, 'quantity': 0},
    3: {'name': 'Lucerne Hay', 'price': 4.55, 'quantity': 0},
    4: {'name': 'Fish food', 'price': 5.68, 'quantity': 0},
    5: {'name': 'Royal Canin', 'price': 6.25, 'quantity': 0},
    6: {'name': 'Pedigree', 'price': 10.35, 'quantity': 0},
    7: {'name': 'Cesar', 'price': 2.94, 'quantity': 0},
    8: {'name': 'Seed Mix', 'price': 11.77, 'quantity': 0},
    9: {'name': 'Dreamies', 'price': 4.07, 'quantity': 0},
    10: {'name': 'Tropical Fish Flakes', 'price': 13.80, 'quantity': 0}
} # dictionaly of the products in the shop

cart = {} # Create a shopping cart dictionary
total_price = 0

def inventory_list(): # function to show list of available products in the shop
    print("In stock:")
    for item_number, item_details in inventory.items():
        print(f"({item_number}) {item_details['name']} - {item_details['price']}£")
    print()
    
def add_item(): # function to add items to the cart
    show_cart = input("Show products in stock? (y/n): ")
    if show_cart == "n":
        pass
    elif show_cart == "y":
        inventory_list()
    else:
        add_item()

    while True: # loop input to add items until 0 is entered
        item_inp = input("(+) Item to add (to stop enter 0): ") # get input of the item to add
        try: # check if number is entered, if not show error
            item = int(item_inp)
        except ValueError:
            item = 0
            print("> Wrong input!")
            break
        
        if item == 0:
            print("Exit 'add to cart'.")
            break
        
        elif item in inventory: # check if item in inventory list
            qnt_inp = input(f"How match items of '{inventory[item]['name']}' to add?: ").replace("-","") # request quantity input
            try: # check if input is a number, if not then show error
                quant = int(qnt_inp)
            except ValueError:
                quant = 0
                print("> Wrong input!")
                add_item() 
            
            if item not in cart:  # check if item not in cart then add item record to cart
                cart[item] = inventory[item].copy()  # Copy the item details to avoid modifying the original inventory
                cart[item]['quantity'] = quant # define quantity of the item
            else:
                cart[item]['quantity'] += quant # if item already in the cart then add quantity input
            print(f"Added {quant} items to the cart.")
        else:
            print("> Wrong input!")

def del_item(): # function to delete items from the cart
    item = 0
    while True: # loop function
        if len(cart) == 0: # check if no items added to cart then show message and exit function
            print("> Your cart is empty!")
            break
        else: 
            pass

        item_inp = input(f"\n(-) Item to delete (to stop enter 0): ") # request item number input to delete
        try: # check if input is a number, if not then error message
            item = int(item_inp)
        except ValueError:
            print("> Wrong input!")
            del_item()
        
        if item == 0: # check if 0 entered then exit function
            print("Exit 'cart edit'.")
            view_cart()
            break

        elif item not in cart: # check if item not in cart then show error message
            print("> No such item in your cart!")
        elif item in cart: # check if item in cart then show name and quantity
            qnt_inp = input(f"You have {cart[item]['quantity']} item(s) of '{cart[item]['name']}' in cart.\nHow much to delete?: ").replace("-","") # request quantity input
            try: # check if input is a number, if not then show error message
                quant = int(qnt_inp)
            except ValueError:
                print("> Wrong input!")
                
            if cart[item]['quantity'] > 0: # check f quantity of the item more than 0 then minus quantity input
              cart[item]['quantity'] -= quant
              if cart[item]['quantity'] < 1: # check if quantity is less than 1 
                  del cart[item] # delete item from cart
        else: # check if item number not in the inventory then show error message
            print("> No such item in the shop!")
            break

def view_cart(): # function to show the cart
    print("Your shopping Cart:")
    total_price = 0 # total price counter
    quant_items = 0 # total items counter
    for item_number, item_details in cart.items(): # show list of added items and details
        print(f"({item_number}) {item_details['name']} - {item_details['quantity']} item(s) / {round(item_details['price'] * item_details['quantity'],2)} GBP")
        total_price += item_details['price'] * item_details['quantity'] # count total price using formula and adding it to counter
        quant_items += item_details['quantity'] # count quantity and adding it to counter
    print(f"Total items: {quant_items}\nTotal price: {round(total_price,2)} GBP")

def write_cart(time): # function to write the cart details
    user_name = input("Enter your full name: ")
    address = input("Enter your full address: ")
    file_name = str(time) +'.txt' 
    ofile = open(file_name,'w')
    total_price = 0 # total price counter
    quant_items = 0 # total items counter
    for num, item_details in cart.items(): # show list of added items and details
        ofile.write(f"{item_details['name']} - {item_details['quantity']} item(s) / {round(item_details['price'] * item_details['quantity'],2)} GBP\n")
        total_price += item_details['price'] * item_details['quantity'] # count total price using formula and adding it to counter
        quant_items += item_details['quantity'] # count quantity and adding it to counter
    ofile.write(f"\nTotal items: {quant_items}\nTotal price: {round(total_price,2)} GBP\n\n")
    ofile.write(f"Customer name: {user_name}\nDelivery address: {address}\n\n")

# start of the program
print("Welcome to PetShop")
while True: # loop input of user actions until exit is chosen
    action = input("\n> 'A' to add items\n> 'E' to edit cart\n> 'V' to view cart\n> 'C' to checkout and exit\nSelect your choice: ").upper() # show menu and request user input
    print()
    if action == 'A': # add items
        add_item()
    elif action =='E': # delete items
        del_item()
    elif action == 'V': # view cart
        view_cart()
    elif action == 'C': # checkout and exit
        date_time = datetime.now()
        f_dtime = date_time.strftime("%Y-%m-%d_%H-%M-%S")
        if len(cart.items()) != 0:
            write_cart(f_dtime)
            print("Thank you for shoping with us!\nGood-bye!\n")
            break
        else:
            print("Your cart is empty!\nGood-bye!\n")
            break           

    else: # check input if wrong then show error message
        print("> Wrong input!")
