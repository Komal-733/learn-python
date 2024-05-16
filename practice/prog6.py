n=4!=7
print(__name__)
print("comment above")
lsi=[3,4]
def sum(lsi,x=5):
  sum=3+2
  print(sum,x)
  print(__name__)
  lsi[0]=2
sum(lsi,x=3)
print(lsi)