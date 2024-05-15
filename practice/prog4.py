a="i3gET3it"
print(a.isalnum())
print(a.find("3",2,6))
print(a.endswith("3",1,6))
print(a.swapcase())
print(a.partition(" "))
print(a.count("3",2))
print(a.lstrip("3"))
c,d,e=0,0,0;f=0
for i in a:
  if i.isupper():
    c+=1
  if i.islower():
    d+=1
  if i.isalpha():
    e+=1
  if i.isnumeric():
    f+=1
print(c,d,e,f)
l=list((1,2,3))
print(l.append("34"))
print(l)
del l[1:3]
print(l)
l.pop(1)
print(l)
l1=list({1:12,2:21})
print(l1)
print(l1[0:2])
l2=list(a)
l2.sort()
print(max(l2))
for i in l2:
  print(i,end="")