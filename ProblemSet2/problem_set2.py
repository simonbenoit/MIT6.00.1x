# PROBLEM 1: PAYING THE MINIMUM

def interest_rate(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance = balance of the payment
    annualInterestRate = self-explaining
    monthlyPaymentRate = self-explaining
    
    """
      
    monthlyInterestRate = (annualInterestRate/12.0)
    totalPaid           = 0
    totalBalance        = 0
    unpaidBalance       = balance
    
    for i in range(1, 13):                            
        minMonthlyPayment = monthlyPaymentRate*unpaidBalance
        monthlyUnpaidBalance = unpaidBalance - minMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
        
        unpaidBalance = updatedBalanceEachMonth
        totalPaid += minMonthlyPayment
        totalBalance += updatedBalanceEachMonth
        
        minMonthlyPayment = round(minMonthlyPayment, 2)
        updatedBalanceEachMonth = round(updatedBalanceEachMonth, 2)
        monthlyUnpaidBalance = round(monthlyUnpaidBalance, 2)
        
        print ("Month: " + str(i))
        print ("Minimum monthly payment: " + str(minMonthlyPayment))
        print ("Remaining balance: " + str(updatedBalanceEachMonth))
        
    totalPaid = round(totalPaid, 2)
    print ("Total paid: " + str(totalPaid))
    print ("Remaining balance: " + str(updatedBalanceEachMonth))
    
# PROBLEM 2: PAYING DEBT OFF IN A YEAR

minPayment = 0
unpaidBalance = 1

while unpaidBalance > 0:
    minPayment += 10
    unpaidBalance = balance
    
    for month in range (1, 13):
        unpaidBalance =  (unpaidBalance - minPayment) *(1+annualInterestRate/12.0)

print "Lowest payment:", minPayment

# PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER 

low = balance / 12.0
high = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0
epsilon = 0.01

minPayment = (high + low) / 2.0
unpaidBalance = balance

for month in range(1, 13):
    unpaidBalance = (unpaidBalance - minPayment) * (1 + annualInterestRate / 12.0)
    
while abs(unpaidBalance) > epsilon:
    if unpaidBalance < 0:
        high = minPayment
    else:
        low = minPayment
        
    minPayment = (high + low) / 2.0
    unpaidBalance = balance
    for month in range(1, 13):
        unpaidBalance = (unpaidBalance - minPayment) * (1 + annualInterestRate / 12.0)

print "Lowest Payment:", round(minPayment, 2)