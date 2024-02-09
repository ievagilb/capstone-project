import math

# load a greeting/welcome message
# write a variable to take in any variation of the words 'investment' or 'bond'e

greeting = input("investment - to calculate the amount of interest you'll earn on your investment\n\
bond       - to calculate the amount you'll have to pay on a home loan\n\n\
Enter either 'investment' or 'bond' from the menu above to proceed: ")

greeting = greeting.lower()

# ask the user to input all the relevant information
if greeting == "investment":
    
    money = int(input("Please enter the amount you would like to deposit:\n"))
    interest_rate = float(input("Please enter your interest rate as percentage (Example: 20):\n"))
    number_of_years = int(input("Please enter number of years you plan on investing:\n"))
    interest_type = input("Please choose if you would like simple or compound interest (enter 'simple' or 'compound'):\n")
    interest_type = interest_type.lower()    

#ask the user to choose between 'simple' or 'compoud' options

    # calculate simple interest
    
    if interest_type == "simple":
        interest_rate = interest_rate / 100
        simple_interest = money *(1 + interest_rate * number_of_years)
        print(f"You have earned a total of", simple_interest, "for this period")

    # calculate compund interest
    elif interest_type == "compound":
        interest_rate = interest_rate / 100
        compound_interest = money * math.pow((1 + interest_rate),number_of_years)
        compound_interest = round(compound_interest, 2)
        print(f"You have earned a total of", compound_interest, "for this period") 
    else:
        print("Please enter either 'simple' or compound'.\nPlease try again")

# calcute the bond option

elif greeting == "bond":

    # ask the user to input all the relevant information
    
    house_value = int(input("Please enter the value of the house:\n"))
    interest_rate = float(input("Please enter your interest rate as percentage (Example: 20):\n"))
    number_of_months = int(input("Please enter the number of months to repay the bond:\n"))

    monthly_rate = (interest_rate/100)/12

    repayment = (monthly_rate * house_value)/(1-(1 + monthly_rate)**(- number_of_months))

    repayment = round(repayment, 2)

    print(f"You're payments will be" ,repayment ,"per calendar month")

else:
    print("Please enter either 'investment' or 'bond'.\nPlease try again")
