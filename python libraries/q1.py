import string
def remove_letter(sentence,letter):
  sen=sentence.split(letter)
  print("".join(sen))
remove_letter('hello there!','e')

def func(s):
  print(string.capwords(s,'h'))
  sen=s.split('h')
  for i in sen:
    sen[sen.index(i)]=i.capitalize()
  sen="".join(sen)
  print(sen)
func("hello there!")