dict={1:2,7:6,2:5,8:5,3:4,5:6,6:5,9:0}
key=list(dict.values())
l=len(key)
for i in range(l):
  for j in range(l-i-1):
    if key[j]>key[j+1]:
      key[j],key[j+1]=key[j+1],key[j]
print(key)