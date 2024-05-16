dict1={1:2,3:4,5:6,7:8}
dict2={1:3,2:4,5:7,6:8}
def addDict(dict1,dict2):
  dict3={}
  dict3=dict1.copy()
  print(dict3)
  dict3.update(dict2)
  print(dict3)
addDict(dict1,dict2)