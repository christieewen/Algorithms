#Python 3.4.2
from nltk.corpus import words
from itertools import permutations

def anagrams_for(word):
  # TODO: 
  # 1. generate permutations of word array (note: don't return itself)
  # 2. check if word is a real word using the syntax below:
  # if "word" in words.words():
  #  print word
  # example using itertools: list(itertools.permutations([1,2,3,4], 2))
  word_array = array('u', word)
  [print new_word.tobytes() 
    for new_word in 
      list(itertools.permutations(word_array, word_array.length)) 
      if new_word in 
        words.words())]
    
anagrams_for("cinema")
