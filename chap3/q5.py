def check(a,b):
  return len(a)==len(b)

b=check("you are wrong","you are right")
if b==True:  
  print("same length")
else:
  print("not same length")