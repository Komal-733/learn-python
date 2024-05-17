def min_dig(n,m):
  d1=n%10
  d2=m%10
  if d1<d2:return n
  else:return m
print(min_dig(491,278))