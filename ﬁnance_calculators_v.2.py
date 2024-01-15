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

# function to loop number check until a user input proper data
def number_check(data): 
    while True:
        number_str = input(data).replace("%", "")
        try:
            number = float(number_str)
            if number > 0:
                return number
            else:
                print("> Wrong input! Please enter a proper number!")
        except ValueError:
            print("> Wrong input! Please enter a number!")

def investment():
    # (P) request money deposit amount
    money_deposit_inp = "Enter your current deposit amount of money: "
    money_deposit = number_check(money_deposit_inp)    
    
    # request rate of investment, if "%" received then replace it with empty space
    interest_rate_invest_inp = "Enter your interest rate (in %): "
    interest_rate_invest_month = number_check(interest_rate_invest_inp)

    # (r) convert the rate input acording to the formula values
    interest_rate_invest = interest_rate_invest_month / 100

    # (t) request number of years to invest
    investing_years_inp = "How many years are you planning to invest: "
    investing_years = number_check(investing_years_inp)

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
    print(f"Your deposit........... {money_deposit}£")
    print(f"Interest rate.......... {round(interest_rate_invest_month)} %")
    print(f"Years to invest........ {round(investing_years)}")
    print(f"Your interest.......... {interest}")
    print("----------------------------------------")
    print(f"Your total amount is... {round(total_amount, 2)}£\n")

def bond():
    # (P) request input of a house value
    house_value_inp = "Enter the present value of the house: "
    house_value = number_check(house_value_inp)
    
    # request user input of interest rate    
    interest_rate_bond_inp = "Enter the interest rate(in %): "
    interest_rate_bond_month = number_check(interest_rate_bond_inp)
    
    # (i) convert input to month value acording to the formula values
    interest_rate_bond = (interest_rate_bond_month / 100) / 12
   
    # (n) request input of number of months
    months_number_inp = "Enter a number of months to repay the bond: "
    months_number = number_check(months_number_inp)
    months_number = int(months_number) 
    
    # calculate repayment using formula | repayment = (i * P) / (1 - (1 + i)**(-n)) |
    repayment = (interest_rate_bond * house_value) / (1 - (1 + interest_rate_bond)**(- months_number))
    
    # print summary and result of calculations
    print("\nSUMMARY")
    print("----------------------------------------")
    print(f"Value of the house..... {house_value}£")
    print(f"Interest rate.......... {round(interest_rate_bond_month)} %")
    print(f"Months to repay........ {months_number}")
    print("----------------------------------------")
    print(f"Your repay each month.. {round(repayment, 2)}£\n")

def start():
    # print program name and instructions 
    print("\n[Finance Calculator]")
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
            return calc
        else:
            # if not then print error message and return to input
            print("> Wrong input! You can choose 'investment' or 'bond' only!")

# the program flow
while True:
    start_quiz = input("Do you want to start? (y/n): ")
    if start_quiz == "y":
        # start of calc program
        calc = start()

        # selecting investment calculations
        if calc == "investment":
            investment()

        # selecting bond calculations
        elif calc == "bond":
            bond()

    elif start_quiz == "n":
        print("\nGood-bye!\n")
        break