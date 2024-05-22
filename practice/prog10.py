import sys
file=open("secondfile.txt","a+")
l1=file.write("hi\n")
sys.stdin.read()
file.close()