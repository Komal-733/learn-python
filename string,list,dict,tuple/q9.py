dict={"january":31,
      "february":28,
      "march":31,
      "april":30,
      "may":31,
      "june":30,
      "july":31,
      "august":31,
      "september":30,
      "october":31,
      "november":30,
      "december":31}

month=input("enter month name -> ")
print(dict[month],"days are there in",month)
key=dict.keys()
lst=list(key)
lst.sort()
print(lst)

for i in dict:
  if dict[i]==31:
    print(i)

lstvalue=[28,30,31]
lstvalue.sort()
for i in lstvalue:
  for j in dict:
    if dict[j]==i:
      print(j,i,end=" ")


