s="bobobwoiefljiaiofjbob"
temp=""
counter=0

for i in range(len(s)-2):
    temp=''
    temp+=s[i]+s[i+1]+s[i+2]
    if temp == "bob" :
        counter+=1
print('Number of times bob occurs is: ', counter)
