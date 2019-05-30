number=input('plz input a integer')
muter=2
l=list(number)
total=0
for i in l:
    i=eval(i)
    total+=i*muter
    muter+=1
CD = 11-total%11
if CD != 10:
    print('CD is:',CD)
else:
    print('CD is X')
