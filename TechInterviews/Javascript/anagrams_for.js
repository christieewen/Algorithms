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
// TODO: optimize using the fact that there are mirror images of the characters in the permutations.
// TODO: permutations function
// Brain storming idea: how about each index is treated as another dimension? For example, [0,1] is 2 dimensions x,y for a 
// 2x2 matrix and [0,1,2] is 3 dimensions for a 2x2x2 and so on.  Perhaps use hyper-cube.  Please note I have no idea 
// what I'm talking about.
var dictionary = ["cinema", "iceman", "love", "evol"];

function anagrams_for(word) {
  var word_char_array = word.split("");
  
  // TODO: iterate through each character shifting/unshifting characters, check if word exists to print
  // Don't use shift/unshift because it is an expensive operation.  Try using a Queue or slice/splice
  
   for (i=0; i < word_char_array.length; i++) {
     for (j=i; j < word_char_array.length; j++){
        word_char_array.splice(j, 0, word_char_array.pop());
        //if (word_char_array.toString() in dictionary) 
        document.write(word_char_array.toString() + "<br>");
       }
    word_char_array.splice(0,0, word_char_array.pop())
   }    
}

function anagrams_for_builtin(word){
  var word_char_array = word.split("");
  
}

anagrams_for("love");
