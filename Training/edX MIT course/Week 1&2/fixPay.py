def fixPay(balance, annualInterestRate ):
    '''
    Finds what fixed monthly payment will be needed to pay off the balance in 12 months
    
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    
    '''    
    
    minimum_fixed_monthly_payment = 10
    monthly_interest_rate = annualInterestRate/12.0 
    test_balance = balance
    while not test_balance <= 0:
        test_balance = balance
        month = 0
        while month < 12:           
            monthly_unpaid_balance = test_balance - minimum_fixed_monthly_payment
            updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
            test_balance = updated_balance_each_month
            month += 1
            # if I don't put this here it will never return 10 
        if test_balance > 0:
            minimum_fixed_monthly_payment += 10
        
    return round(minimum_fixed_monthly_payment, 2 )
print('Lowest Payment:', fixPay(33295, 0.2))

