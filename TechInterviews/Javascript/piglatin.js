function getPigLatin(word) {
  var firstLetter = word.charAt(0);
  var pigLatin = "";
  switch (firstLetter) {
    'a':
    'e':
    'i':
    'o':
    'u':
    'y':
      pigLatin = word.concat("ay");
      break;
    default:
      pigLatin = word.splice(1).concat(firstLetter, "ay");  
  }
  console.log(pigLatin);
}
