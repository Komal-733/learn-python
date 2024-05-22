myfile=open("firstfile.txt","r+")
print(myfile.read())
myfile.write("hello world"+"\t")
myfile.flush()

myfile.close()