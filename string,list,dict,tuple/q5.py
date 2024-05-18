sen=input("enter a sentence -> ")
sen.lstrip()
sen.rstrip()
sen=sen+" "
ind=0;l=0
word=''
for i in range(len(sen)):
  if sen[i]==" ":
    word=sen[ind:i]
    if l<len(word):
      l=len(word)
      start=ind
      end=i
    ind=i+1
print(sen[start:end])