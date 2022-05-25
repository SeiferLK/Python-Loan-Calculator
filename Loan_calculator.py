import math
import argparse

    
# Initialising the Argument Parser
    
parser = argparse.ArgumentParser(
    description="This is a Differentiate Loan Repayment Calculator"
)
    
parser.add_argument("--type", default="annuity", choices=["annuity", "diff"], 
    help="These are the payment options. Input either 'annuity' or 'diff'."
    )
parser.add_argument("--payment", type=int,
    help="This is the montly payment amount.")
parser.add_argument("--principal", type=int,
    help="This is the principal loan total.")
parser.add_argument("--periods", type=int,
    help="This is the total number of payments.")
parser.add_argument("--interest", type=float,
    help="This is the agreed upon interest rate.")
        
args = parser.parse_args()  
    
# Creating an easy-to-use "Incorrect Parameters" return function  
    
def incorrect_parameters():
    print("Incorrect parameters")
    quit()
    
### Validation Checks  
    
    # Validation check for type

def type_validation():
    if args.type is None or not "diff" or not "annuity":
        incorrect_parameters()
            
    # Validation checks for diff        
            
def diff_validation():
    if args.type == "diff":
        if args.payment is not None:
            incorrect_parameters()
                
def diff_validation2():
    if args.type == "diff":
        if args.interest is None:
            incorrect_parameters()
                
    # Validation check for annuity

def annuity_validation():
    if args.type == "annuity":
        if args.interest is None:
            incorrect_parameters()

    # Validation check for the number of arguments when type = diff

def argument_validation_diff():
    if args.type == "diff":
        if args.principal is None and args.periods is None and args.interest is None:
            incorrect_parameters()   
                
### End of validation checks                 
      
# Setting the calculation for nominal interest, from the interest rate given

if args.interest is not None:
    nominal_interest =  float(((args.interest) * (0.01) / 12))      

# Initial validation

type_validation()
      
# For when type == annuity

if args.type == "annuity":
    annuity_validation()
    if args.principal is None:
        annuity = args.payment
        months = args.periods
        numerator = nominal_interest * (1 + nominal_interest) ** months
        denominator = ((1 + nominal_interest) ** months) - 1
        num_dom = numerator / denominator
        loan_principal = annuity / num_dom
        print("Your loan principal = " + str(loan_principal) + "!")
    elif args.payment is None:
        loan_principal = args.principal
        months = args.periods
        numerator = nominal_interest * (1 + nominal_interest) ** months
        denominator = ((1 + nominal_interest) ** months) - 1
        annuity = loan_principal * (numerator / denominator)
        total_payment = math.ceil(annuity) * months
        overpaid_amount = math.ceil(total_payment) - math.ceil(loan_principal)
        print("Your monthly payment = " + str(math.ceil(annuity)) + "!")
        print("Overpayment = " + str(math.ceil(overpaid_amount)))
    elif args.periods is None:
        loan_principal = args.principal
        annuity = args.payment
        months = math.ceil(math.log((annuity / (annuity - nominal_interest * loan_principal)), 1 + nominal_interest))
        total_payment = annuity * months
        overpaid_amount = total_payment - loan_principal
        if months < 12:
            print("It will take " + str(months) + " months to repay this loan!")
            print("Overpayment = " + str(overpaid_amount))
        elif months == 12:
            print("It will take 1 year to repay this loan!")
            print("Overpayment = " + str(overpaid_amount))
        elif months > 12:
            years = months / 12
            mon = months % 12
            if mon > 1:
                print("It will take " + str(math.ceil(years)) + "years and " + str(months) + " months to repay this loan!")
                print("Overpayment = " + str(overpaid_amount))
            else:                 
                print("It will take" + str(math.ceil(years)) + " years and 1 month to repay this loan!")
                print("Overpayment = " + str(overpaid_amount))  
        else:
            incorrect_parameters()
                
# For when type == diff

elif args.type == "diff":
    diff_validation() # Validation checks associated with diff
    diff_validation2()
    loan_principal = args.principal
    months = args.periods
    numerator = nominal_interest * (1 + nominal_interest) ** months
    denominator = ((1 + nominal_interest) ** months) - 1
    annuity = loan_principal * (numerator / denominator)
    total_payment = 0
    m = months
    for m in range(1, months + 1):
        dm = (loan_principal / months) + nominal_interest * (loan_principal - (loan_principal * (m - 1)) / months)
        print("Month " + str(m) + ": payment is " + str(math.ceil(dm)))
        total_payment += math.ceil(dm)
    overpaid_amount = total_payment - loan_principal 
    print("Overpayment = " + str(overpaid_amount))     
