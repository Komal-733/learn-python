N=int(input("enter a number"))
s=0
if(N>=0):
  for i in range(N,2*N+1):
    s+=i
  print(s)
else:
  for i in range(2*N,N+1):
    s+=i
  print(s)