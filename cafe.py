#---------------------------------------------------------------------#
# define dictionaries: menu, stock, price
# print products quantity, names, prices using for loop
# print total worth of all items in stock
#---------------------------------------------------------------------#
# define list of products names
menu = {1:'Green Tea',
        2:'Cola',
        3:'Capuchino',
        4:'Latte',
        5:'Water'} 

# define list of products quantity in stock
stock = {1: 6,
         2: 8,
         3: 5,
         4: 2,
         5: 0} 

# define list of product prices
price = {1: 2.34,
         2: 1.45,
         3: 3.56,
         4: 2.66,
         5: 0.88} 

total_stock = 0 # total price counter

print("\nMy Cafe\nLeft in stock:")
for id, quant in stock.items():
        total_stock += quant * price[id]
        # print products quantity, names, prices
        if quant != 0:
            print(f"+| {quant} | {menu[id]} - {price[id]}£")
        if quant == 0:
            print(f"-| {quant} | {menu[id]} - {price[id]}£")
# print total stock worth of all items in stock
print(f"\nTotal worth: {round(total_stock,2)}\n") 

# Alternative approach

# define single dictionary of products with all details
# stock_list = {1: {'name': 'Green Tea', 'price': 2.34, 'stock': 0},
#               2: {'name': 'Cola', 'price': 1.45, 'stock': 2},
#               3: {'name': 'Capuchino', 'price': 3.56, 'stock': 0},
#               4: {'name': 'Latte', 'price': 2.66, 'stock': 6},
#               5: {'name': 'Water', 'price': 0.66, 'stock': 9} }

# total_stock = 0 # total price counter

# for id, product in stock_list.items(): # print products quantity, names, prices
#         total_stock += product['stock'] * product['price']
#         print(f"| {product['stock']} | {product['name']} - {product['price']}£")
       
# print(f"\nTotal worth: {round(total_stock,2)}\n") # print total stock worth of all items in stock 