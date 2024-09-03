
thisdict={"a":1,"keys":'hello',"c":[2,5.5]}
for i in thisdict:
  print(i,thisdict[i]) 
alpha=65
c=0
for i in range(1,4):
  for j in range(1,i+1+c,1):
    print(chr(alpha),end="")
  print("\r")
  alpha+=1
  c+=1
print(thisdict) 
s=input("enter a sentence")
slower=s.lower()
count=0
for i in slower:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    count+=1
print(count)
print("count"*3)
print(ord("a"))
print(chr(65))
print(s[2:-10])
print(len(s))
sen="hello"