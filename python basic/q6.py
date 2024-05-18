def  func1(feet):
  inch=feet*12
  return inch
def func2():
  feet=int(input("enter the lenght in feet"))
  return feet
def func3():
  feet=func2()
  print(func1(feet))
func3()