// 
// Example of a recursive Binary Search Tree from Binary vs. Linear Searching from 
// http://meetupresources.herokuapp.com/whiteboard.html
//
// Write an example demonstrating Binary Search. Write an example demonstrating Linear Search. 
// Hint: A linear search looks down a list, one item at a time, without jumping. 
// In complexity terms this is an O(n) search - the time taken to search the list gets bigger at the same rate as the list does. 
// A binary search is when you start with the middle of a sorted list, and see whether that's greater than or less than the value 
// you're looking for, which determines whether the value is in the first or second half of the list.


var node = function(key) {
  this.key = key;
  this.left = null;
  this.right = null;
};

function binary_search_recursive(key, node) {
  if (node.key == key or node == null) 
    return node;
  else if (key < node.key) 
    binary_search_recursive(key, node.left);
  else
    binary_search_recursive(key, node.right); 
}


// TODO: create, insert, delete
