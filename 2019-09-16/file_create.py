a=open('AS_CS_opt2_gradebook.txt','w')
import random
mathg=0
csg=0
hpyg=0
total_mathg=90*12
total_csg=95*12
total_phyg=88*12
first_names=['Daniel','Julian','Lisa','shirley','Nico','Tim',
             'James','Andy','Cathy','Brian','Harry','Jack']
family_names=['Chu','Ye','Xu','Zeng','Jiang','Xing',
              'Liu','Zhang','Yang','Shan','Fang','Jin']
for i in range(11):
    mathg=random.randint(85,95)
    csg=random.randint(92,97)
    phyg=(random.randint(84,92))
    a.write(first_names[i]+' '+family_names[i]+ " " +str(mathg)+' '+str(csg)+ " " +str(phyg)+'\n')
    total_mathg-=mathg
    total_csg-=csg
    total_phyg=phyg
a.write(first_names[11]+' '+family_names[11]+ " " +str(total_mathg)+' '+str(total_csg)+ " " +str(total_phyg)+'\n')

a.close()