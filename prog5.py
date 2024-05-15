l1=['a','b','c']
l2=['h','i','t']
l3=['0','1','2']
l1.extend(l2)
l1.insert(0,l3)
print(l1)
t1=tuple("apple")
c=0
for i in t1:
  c+=1
  if "l"==i:
    break
print(c-1)
dict={1:2,3:4,5:1,7:8,9:0}
for i in dict:
  if dict[i]==3:
    print(i)
l3.reverse()
print(l3)
l9=list()
print(type(l9))
t4=tuple()
print(type(t4))
dict1={}
print(type(dict1))
