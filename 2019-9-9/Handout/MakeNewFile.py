def MakeNewFile():
    a=open("NewEmailDetails.txt",'w')
    b=open("EmailDetails.txt",'r')
    c=b.readline()
    
    while len(c)>0:
        c='00'+c
        a.write(c)
        c=b.readline()
    a.close()
    b.close()

def IsEmailValid(email):
    valid=True        
    if email[0]=='@':
        valid=False
    at_found=False
    for i in range(len(email)):
        if email[i]=='@':
            at_found=True
            break
    if at_found==False:
        valid=False
    if len(email[i:])<3:
        valid=False
    return valid
