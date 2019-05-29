balance=42
AIR=0.2
MIR=AIR/12
MPR=0.04
for i in range(1,13):
    huanKuan=balance*MPR
    balance-=huanKuan
    balance=round(balance*(1+MIR),2)
    print("Month {} Remaining balancce:".format(i), balance)
print("Remaining balance:",balance)
