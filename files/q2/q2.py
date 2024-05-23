f1=open('files/q2/sports.dat','r')
f2=open('files/q2/athletics.dat','w')
data=f1.readlines()
for i in data:
  j=i.split(' ~ ')
  if j[0]=='athletics':
    f2.write(j[1])
f1.close()
f2.close()