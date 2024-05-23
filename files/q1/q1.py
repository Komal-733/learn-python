import string
f1=open('files/q1/q1a.txt','r')
f2=open('files/q1/q1b.txt','w')
a=f1.read()
a=string.capwords(a)
f2.write(a)
f1.close()
f2.close()