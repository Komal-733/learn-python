import random
def gen(n):
  d=n;r=1;l=9
  while(n>1):
    r*=10
    l=l*10+9
    n-=1
  return random.uniform(r,l)
print(gen(2))