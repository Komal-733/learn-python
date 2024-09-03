import math
for i in range(1,6):
  for j in range(1,i):
    print("*",end='')
  print('\r')
for i in range(6,1,-1):
  for j in range(1,i):
    print("*",end='')
  print('\r')
"""
This is a comment
written in more than just one line
"""
print("Hello, World!")
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1)
List = []
print("Initial blank List: ")
print(List)
List.append(1) 
List.append(2)
print("List after Addition of Three elements: ")
print(List)
List.insert(2, 12)
print("List after performing Insert Operation: ")
print(List)
List.insert(2, 1)
print("List after performing Insert Operation: ")
print(List)
print(math.sqrt(25))

A=[1,2,
3]
B='XYZ'
Res=zip(A,B)
print(Res)# list of tuples print(Res)
a=20
def display():
  global a = 30
  print('value of a is',a)
display()
print('the value of an outside function is',a)
