def getPigLatin(word):
  firstLetter = word.slice(word, 1, 1)
  if firstLetter in ['a', 'e', 'i', 'o', 'y']
    word.append("ay")
  else
    word.append(firstLetter)
    word.append("ay")
  print word
  
