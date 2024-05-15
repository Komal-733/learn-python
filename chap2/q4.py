lst=list(input("enter  a list -> "))
l=len(lst)
last=lst[l-1]
for i in range(l-1,0,-1):
  lst[i]=lst[i-1]
lst[0]=last
print(lst)