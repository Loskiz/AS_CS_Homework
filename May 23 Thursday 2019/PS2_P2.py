AIR=0.2
MIR=AIR/12
payment=0
while balance>0:
    balance=4773
    payment+=10
    for i in range(12):
        balance=balance-payment
        balance=balance*(1+MIR)
print(payment)
