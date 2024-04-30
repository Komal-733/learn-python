firsttime=int(input("Please enter the first time : "))
secondtime=int(input("Please enter the second time : "))
min1=firsttime%100
min2=secondtime%100
hour1=firsttime//100
hour2=secondtime//100
calcmin=min2-min1
calchour=hour2-hour1
if(calcmin>=0):
  print(calchour,"hours",calcmin,"minutes")
else:
  print(calchour-1,"hours",60+calcmin,"minutes")