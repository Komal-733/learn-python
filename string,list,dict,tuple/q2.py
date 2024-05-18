sentence=input("Enter  a sentence -> ")
sentence.lstrip()
sentence.rstrip()
sentence+=" "
count=sentence.count(" ")
print(count)
length=len(sentence)
print(length)
c=0
for i in sentence:
  if i.isalnum():
    c+=1
per=c*100/length
print(per)