import math

# investmant - to calculate the amount of interest you'll earn on your investment
# bond - to calculate the amount you'll have to pay on a home loan


#Investment calculator function
def investment_calculator():
    #inputting details of investment
    principal = float(input("Enter the principal amount:"))
    rate = float(input("Enter the annual interest rate(%):")) / 100
    time = float(input("Enter the investment time period (years):"))

#get the user's choice for typer of interest
    print("Choose the type of interest:")
    print("1. Simple interest:")
    print("2. Compound interest:")
    interest_type = int(input())

# calc based on interest type
    if interest_type == 1:
        investment_amount = principal * (1 + (rate * time))
    elif interest_type == 2:
        investment_amount = principal * math.pow((1+ rate), time)
    else:
        print("invalid choice. Please choose either `simple` or `compound`.")
    # issue here?
    
    print("Investment amount after", time, "years", round(investment_amount, 2))


#Define the bond calculator function the plan is to return the monthly payment.
def bond_calculator():
    #input the bond info
    present_value = float(input("Enter the principal amount:"))
    interest_rate = float(input("Enter the interest rate:")) / 100 /12 #converted to monthly
    num_payments = int(input("Enter the number of payments:"))

    #calculate the monthly repayment
    repayment = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-num_payments))
    #display results
    print("The monthly repayment amount is: {:.2f}".format(repayment))
  


# Display the menu and get user's choice
print("Choose a calculator:")
print("1. Investment calculator:")
print("2. Bond calculator:")
choice = int(input())

# Call the appropriate function based on user's choice
if choice == 1:
    investment_calculator()
elif choice == 2:
    bond_calculator()
else:
    print("Invalid choice. Please choose either 1 or 2.")




    