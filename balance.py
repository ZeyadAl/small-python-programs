'''
we are given 3 variablees
1) balance
2) annual interest rate
3) monthly min rate

first calculate monthly interest rate

'''

balance= float(input('Balance '))
annual= float(input('Annual interest rate '))
minrate= float(input('monthly Min rate '))
paid=0
mint= annual/12
for i in range(12):
    balance= balance*(mint+1)
    balance-=balance*minrate
    paid+=balance*minrate
    print(round(balance, 2))
print ('remaining balance', str(round(balance, 2)), str(paid))
