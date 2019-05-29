balance=320000
AIR=0.2
MIR=AIR/12
lower=balance/12
upper=(balance*(1+MIR)**12)/12
payment=0
ubalance=1
while abs(ubalance)>0.05:
    if ubalance<0:
        upper=payment
    else:
        lower=payment
    ubalance=balance
    payment=(lower+upper)/2
    for i in range(12):
        ubalance=ubalance-payment
        ubalance=ubalance*(1+MIR)
'''
while balance>0:
    balance=4773
    payment+=10
    for i in range(12):
        balance=balance-payment
        balance=balance*(1+MIR)
'''
print(round(payment,2))
