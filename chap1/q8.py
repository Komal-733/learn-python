def arrange(date):
  year=int(date%10000)
  date=date//10000
  date=int(date%100)
  month=date//100-1
  monthname=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
  print(monthname[month]," ",date,", ",year,sep="")
date=int(input("Enter date : "))
arrange(date)