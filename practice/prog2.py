import math
a=15
print(a)
b=10
print(b)
if(a>b):
  print(1)
  pass
print(10)
for i in range (0,100,2):
  if(i==2 or i==5):
    pass
  else:
    print("Ha fool!" ,end=" ")
print(14%12//14)
print(int(13.25+4/2))
print(8/4/2)
print(float('12'))
print("hello\\example\\test.txt")
print('''EINA
mina
dika''')
def inner():
  title= "another title"
  print(title)
inner()
a=10
print(max(3,4,5))
ranges= int(input("enter the range"))
for i in range(2,ranges+1):
  count=0
  for j in range(2,i):
    if i%j==0:
      count+=1
  if(count==0):
    print(i,end=" ")
for i in range(5,0,-1):
  print(i)
