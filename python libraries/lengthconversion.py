#lengthconversion.py
'''for the conversion of various length'''

def miletokm(mile):
  '''convert length mile to km'''
  km=mile*1.609344
  return km

def kmtomile(km):
  '''convert length km to mile'''
  mile=km/1.609344
  return mile

def feettoinches(feet):
  '''convert length feet to inches'''
  inch=12*feet
  return inch

def inchestofeet(inch):
  '''convert length inches to feet'''
  feet=inch/12
  return feet

#constants
mile=1.609344
feet=12
