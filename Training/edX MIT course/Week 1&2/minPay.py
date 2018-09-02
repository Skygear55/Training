def minPay(balance, annualInterestRate, monthlyPaymentRate ):
    '''
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal
    '''
    monthly_interest_rate = annualInterestRate/12.0  
    for month in range(12):        
        minimum_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance_each_month
    return round(updated_balance_each_month, 2 )
print('Remaining balance:', minPay(484, 0.2, 0.04))


for month in range(12): 
        monthly_unpaid_balance = balance - minimum_fixed_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance_each_month