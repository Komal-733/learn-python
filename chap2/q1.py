phonenum=input("Enter a phone number of format 000-000-0000 -> ")
c=0
if phonenum.isalpha():
  print("wrong format")
else:
  if phonenum[3]=="-" and phonenum[-5]=="-":
    for i in phonenum:
      if i.isdigit():
        c+=1
    if c==10:
      print(phonenum,"is a legal input")
    else:
      print("wrong format")
  else:
      print("wrong format")