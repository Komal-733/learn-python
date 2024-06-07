'''list=[3,6,8,17,20,24,30]
key=17
index=3
l=len(list)
lower=list[0]
higher=list[l-1]
m=list[index]
c=0;i=0
while m>0:
  if m>key:
    m=list[index+i]
    i+=3
  elif m==key:
    c+=1
  else:
    for i in range(list[i-index],m,1):
      if i == key:
        c+=1
if c!=0:
  print("present")'''
print('c')
print('m,list[i-index]')