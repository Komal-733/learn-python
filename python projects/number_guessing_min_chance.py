import math
import random
start=int(input("enter starting range:"))
end=int(input("enter ending range:"))
ran_choose=random.randint(start,end)
min_chance=math.ceil(math.log(end-start+1,2))
chance=0
while(chance<min_chance):
  guess=int(input("enter guess:"))
  if guess<ran_choose:
    print("guess is too small")
  elif guess>ran_choose:
    print("guess is too large")
  else:
    print("guess is right")
    break
  chance+=1
if(chance>=min_chance):
  print("number of chance exceeded")