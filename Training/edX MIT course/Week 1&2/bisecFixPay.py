def bisecFixPay(balance, annualInterestRate ):
    '''
    Finds what fixed monthly payment will be needed to pay off the balance in 12 months
    
    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    
    '''    
    epsilon = 0.2
    monthly_interest_rate = annualInterestRate/12.0 
    low = balance/12
    high = (balance*(1 + monthly_interest_rate)**12)/12.0
    guess = (high + low)/2
    test_balance = balance
    while  test_balance > epsilon:  
        test_balance = balance
        for month in range(12):    
            monthly_unpaid_balance = test_balance - guess
            updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
            test_balance = updated_balance_each_month   
        if test_balance > epsilon:
            high = guess                  
        elif test_balance < -epsilon :
            low = guess
        else:
            break                
        guess = (high + low)/2 
        
    
                       


                    
    minimum_fixed_monthly_payment = guess
    return round(minimum_fixed_monthly_payment, 2 )
print('Lowest Payment:', bisecFixPay(320000, 0.2))

#working code below 

init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))








