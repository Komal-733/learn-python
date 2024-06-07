for i in range(1,6):
  for j in range(i,5):
    print(" ",end='')
  for k in range(i):
    print("* ",end='')
  print('\r')
for i in range(1,5):
  for j in range(i):
    print(" ",end='')
  for k in range(i,5):
    print("* ",end='')
  print('\r')
for i in range(1,4):
  for j in range(i,5):
    print(" ",end='')
  for k in range(i*2-1):
    print("*",end='')
  print('\r')