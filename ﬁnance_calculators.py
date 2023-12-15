'''
Current extended solution is added as a sample which consists checks to exclude the users wrong 
type of inputs. E.g. characters when only digits are expected. Also some input checks can 
validate unnormal value inputs that won't be expected in real life e.g. an interest rate more 
than 100. The approach is to make a 'bottleneck' input validation where the user can not input 
anything except expected values which exclude further bugs while the program usage. This approach
needs more time for coding but takes less time for further bugs testing. 
'''

# the formula inside the program needs math import at the beginning
import math

print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond -       to calculate the amount you'll have to pay on a home loan\n")

# loop check until the proper type is entered 
while True:
    calc = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    if calc == "investment" or calc == "bond":
        break
    else:
        print("> You've done wrong input!")

if calc == "investment":
    
    # loop check until the proper type is entered 
    while True:
        # P in formula
        money_deposit = input("Enter your current deposit amount of money: ")
        
        if money_deposit.isdigit():
            break
        else:
            print("> Wrong input! Please enter a number!")

    # final casting to float type    
    money_deposit = float(money_deposit)
    
    # loop check until the proper type is entered 
    while True:
        # r in formula
        interest_rate_invest = input("Enter your interest rate (in %): ").replace("%", "")
       
        if interest_rate_invest.isdigit() and 0 < int(interest_rate_invest) <= 100:
            break
        else:
            print("> Wrong input! Please enter correct number of interest rate!")

    # need to divade value by 100 for further calculations 
    interest_rate_invest = float(interest_rate_invest) / 100

    while True:
        # t in formula
        investing_years = input("How many years are you planning to invest: ")
       
        if investing_years.isdigit() and 0 < int(investing_years) <= 300:
            break
        else:
            print("> Wrong input! Please enter correct number of investing years!")

    # final casting to int type
    investing_years = int(investing_years)

    #loop check until the proper type is entered 
    while True:
        interest = input("Enter either your interst is 'simple' or 'compound': ").lower()

        if interest == "simple" or interest == "compound": 
            break
        else:
            print("> Wrong input! The only 'simple' or 'compound' are acceptable!")
    
    if interest == "simple":

        # A in formula | A = P *(1 + r*t) |
        total_amount = money_deposit * (1 + interest_rate_invest * investing_years)
    
        print(f"\nYour total amount when simple interest will be: {round(total_amount, 2)} pounds.\n")
    
    elif interest == "compound":

        # A in formula | A = P * math.pow((1 + r), t ) |
        total_amount = money_deposit * math.pow((1 + interest_rate_invest), investing_years)
      
        print(f"\nYour total amount when compound interest will be: {round(total_amount, 2)} pounds.\n")

elif calc == "bond":
    
    while True:
        # P in formula
        house_value = input("Enter the present value of the house: ")
        
        if house_value.isdigit():
            break
        else:
            print("> Wrong input! Please enter a number!")

    # final casting to float type
    house_value = float(house_value)
        
    while True:
        # i in formula
        interest_rate_bound = input("Enter the interest rate(in %): ").replace("%", "")
        
        if interest_rate_bound.isdigit() and 0 < float(interest_rate_bound) <= 100:
            break
        else:
            print("> Wrong input! Please enter correct number of interest rate!")
    
    # need to convert value into month value for further calculations
    interest_rate_bound = (float(interest_rate_bound) / 100) / 12
   
    while True:
        # n in formula
        months_number = input("Enter the number of months you plan to take to repay the bond: ")
        
        if months_number.isdigit() and 0 < int(months_number) < 3600:
            break
        else:
            print("> Wrong input! Please enter correct number of months!")

    # final casting to int type
    months_number = int(months_number)
    
    # calculating repayment using formula | repayment = (i * P) / (1 - (1 + i)**(-n)) |
    repayment = (interest_rate_bound * house_value) / (1 - (1 + interest_rate_bound)**(- months_number))

    print(f"\nYou will have to repay each month: {round(repayment, 2)} pounds.\n")