def remove_letter(sentence,letter):
  sen=sentence.split(letter)
  for i in sen:
    print(i,end='')
remove_letter('hello there!','e')