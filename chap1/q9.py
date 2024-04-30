num=int(input("ENTER TOTAL NUMBER OF CONVERSION "))
miles=0.0
for i in range(0,num):
  miles=float(input("Enter value in miles"))
  kilo=float(miles*1.6)
  print(miles,kilo)