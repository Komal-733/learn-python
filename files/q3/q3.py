f1=open('files/q3/data.txt','r')
f2=open('files/q3/updatedata.txt','w')
d=f1.readlines()
for i in d:
  s=i.split(' ')
  p=s[0],'\t',s[1]
  f2.writelines(p)
f1.close()
f2.close()