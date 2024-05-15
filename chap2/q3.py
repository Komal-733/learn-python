list1=eval(input("enter a list in number -> "))
list2=eval(input("enter a list in number of same size as above -> "))
list3=[]
length=len(list1)
l=len(list2)
list3=[]
print(list1)
print(list2)
if(length != l):
  print("list size are not same")
else:
  for i in range(min(length,l)):
    list3.append(list1[i]+list2[i])
print(list3)