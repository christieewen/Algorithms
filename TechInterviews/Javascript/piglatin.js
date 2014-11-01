function getPigLatin(word) {
  var firstLetter = word.charAt(0);
  var pigLatin = "";
  if firstLetter in ['a', 'e', 'i', 'o', 'y']
    pigLatin = word.concat("ay");
  else
    pigLatin = word.splice(1).concat(firstLetter, "ay");
  console.log(pigLatin);
}
