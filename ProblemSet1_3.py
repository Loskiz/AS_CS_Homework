#set up
s = 'azcbobobegghaklabcsaaa'
s+='1'
temp=""
alphbs=[]

#find strs in order
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        temp+=s[i]
    else:
        temp+=s[i]
        if len(temp) !=1:
            alphbs.append(temp)
        temp=''
print(alphbs)

#determine max len str
maxlenstr=alphbs[0]
for j in alphbs:
    if len(j)>len(maxlenstr):
        maxlenstr=j
print(maxlenstr)
