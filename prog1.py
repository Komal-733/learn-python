import math
def fruits():
  fruit=input("What is your favourite fruit?")
  a=int(input())
  b=a**3
  print(b)
  print(math.cbrt(b))
  print(fruit+" "+fruit)
  print("I\'ve eaten",a,fruit)
  complex=3+8j
  a=bool(5)
  print(a)
  print(complex.imag)
  print(type(complex))
  list=[2,3,3]
  tuple=(4,5,5)
  print(list)
  print(tuple)
  dict={2:4,5:2,6:4}
  print(dict)
  print(dict[2])
  print(dict[5])
  print(dict.get(4,"3"))
fruits()