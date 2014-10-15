// Anagrams
//
// An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema. 
// We're going to write a method called anagrams_for that takes as its input a word and an array of words, 
// representing a dictionary, and returns an array consisting of all the anagrams of the input word. anagrams_for should 
// return an empty array ([]) if no anagrams are found in the dictionary. You don't have to worry about the order of the 
// returned Array.
// http://meetupresources.herokuapp.com/whiteboard.html
//
// array methods implementation
// TODO: hash method implementation
//
var dictionary = ["cinema", "iceman"];

function anagrams_for(word) {
  var new_word;
  // TODO: iterate through each character shifting/unshifting characters, check if word exists to print
  // Don't use shift/unshift because it is an expensive operation.  Try using a Queue or slice/splice
  for (i=0; i < new_word.length; i++) {
      var pivot = word.shift(); // remove the first letter
      word.unshift(word.pop()); // remove the last and place in beginning
      var new_word = pivot.concat(word);
      for (j=i; )
      if (new_word in dictionary) 
        print word;
      }

}



anagrams_for("cinema");
