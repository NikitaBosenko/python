#-------------------------------------------------------------------------------------------#
# print program name and instructions
# request user input 'investment' or 'bond'
# if 'investment' then ask user input:
    # money deposit
    # interest name
    # years to invest

    # request user input 'simple' or 'compound'
    # if 'simple' then calculate total amount using formula [ A = P *(1 + r*t) ]
    # if 'compound' then calculate total amount using formula [ A = P * math.pow((1 + r), t ) ]
    
    # print summary and result of calculations

# if 'bond' then ask user input:
    # house value
    # interest rate
    # months to invest

    # calculate repayment using formula [ repayment = (i * P) / (1 - (1 + i)**(-n)) ]

    # print summary and result of calculations
#-------------------------------------------------------------------------------------------#

# the formula inside the program needs math import
import math

# print program name and instructions 
print("[Finance Calculator]")
print("-------------------------------------------------------------------------------")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("      bond - to calculate the amount you'll have to pay on a home loan")
print("-------------------------------------------------------------------------------")

# loop check until the proper type is entered 
while True:
    # request input either 'investment' or 'bond', converting input to lower case
    calc = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    # check if input is 'investment' or 'bond'
    if calc == "investment" or calc == "bond":
        # if yes then break the loop
        break
    else:
        # if not then print error message and return to input
        print("> Wrong input! You can choose 'investment' or 'bond' only!")

# selecting investment calculations
if calc == "investment":
    
    # loop check until the proper type is entered 
    while True:
        # (P) request money deposit amount
        money_deposit = input("Enter your current deposit amount of money: ")
        # check if input is a number
        try: 
            # try casting the input to float type if customer wants to see pences also
            money_deposit = float(money_deposit)
           
            # check if the number more than 0
            if money_deposit > 0:
            # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")

        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")
    
    # loop check until the proper type is entered 
    while True:
        # request rate of investment, if "%" received then replace it with empty space
        interest_rate_invest_input = input("Enter your interest rate (in %): ").replace("%", "")
        
        # check if inpunt is a number
        try:
            # try to cast input to float
            interest_rate_invest = float(interest_rate_invest_input)
            # check if the number more than 0
            if interest_rate_invest > 0:
                # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")
        
        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")

    # (r) convert the rate input acording to the formula values
    interest_rate_invest = interest_rate_invest / 100

    while True:
        # (t) request number of years to invest
        investing_years = input("How many years are you planning to invest: ")
        
        # check if inpunt is a number
        try:
            # try to cast input to integer
            investing_years = int(investing_years)
            # check if the number more than 0
            if investing_years > 0:
                # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")
        
        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")

    #loop check until the proper type is entered 
    while True:
        # request either 'simple' or 'compound' calculations, converting input to lower case
        interest = input("Enter either your interst is 'simple' or 'compound': ").lower()
        
        # check if input either 'simple' or 'compound'
        if interest == "simple" or interest == "compound": 
            # if yes then break the loop
            break
        else:
            # if not then print error message and return to input
            print("> Wrong input! You can choose 'simple' or 'compound' only!")
    
    # selecting simple calculations
    if interest == "simple":

        # (A) calculate total amount using formula | A = P *(1 + r*t) |
        total_amount = money_deposit * (1 + interest_rate_invest * investing_years)
    
    # selecting compound calculations
    elif interest == "compound":

        # (A) calculate total amount using formula | A = P * math.pow((1 + r), t ) |
        total_amount = money_deposit * math.pow((1 + interest_rate_invest), investing_years)
        
    # print summary and result of calculations
    print("\nSUMMARY")
    print("----------------------------------------")
    print(f"Your deposit........... {money_deposit} pounds")
    print(f"Interest rate.......... {interest_rate_invest_input} %")
    print(f"Years to invest........ {investing_years}")
    print(f"Your interest.......... {interest}")
    print("----------------------------------------")
    print(f"Your total amount is... {round(total_amount, 2)} pounds\n")

# selecting bond calculations
elif calc == "bond":
    
    while True:
        # (P) request input of a house value
        house_value = input("Enter the present value of the house: ")
        # check if inpunt is a number
        try:
            # try to cast input to float
            house_value = float(house_value)
           
            # check if the number more than 0
            if house_value > 0:
                # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")
        
        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")
        
    while True:
        # request user input of interest rate
        interest_rate_bond_input = input("Enter the interest rate(in %): ").replace("%", "")
        # check if inpunt is a number
        try: 
            # try to cast input to float
            interest_rate_bond = float(interest_rate_bond_input)
            
            # check if the number more than 0
            if interest_rate_bond > 0:
                # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")
        
        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")
    
    # (i) convert input to month value acording to the formula values
    interest_rate_bond = (interest_rate_bond / 100) / 12
   
    while True:
        # (n) request input of number of months
        months_number = input("Enter a number of months to repay the bond: ")
        # check if inpunt is a number
        try:
            # try to cast input to integer
            months_number = int(months_number)
            # check if the number more than 0
            if months_number > 0:
                # if yes then break the loop
                break
            else:
                # if not then print error message and return to input
                print("> Wrong input! Please enter a proper number!")
        
        except ValueError:
            # if not then print error message and return to input
            print("> Wrong input! Please enter a number!")
    
    # calculate repayment using formula | repayment = (i * P) / (1 - (1 + i)**(-n)) |
    repayment = (interest_rate_bond * house_value) / (1 - (1 + interest_rate_bond)**(- months_number))
    
    # print summary and result of calculations
    print("\nSUMMARY")
    print("----------------------------------------")
    print(f"Value of the house..... {house_value} pounds")
    print(f"Interest rate.......... {interest_rate_bond_input} %")
    print(f"Months to repay........ {months_number}")
    print("----------------------------------------")
    print(f"Your repay each month.. {round(repayment, 2)} pounds\n")