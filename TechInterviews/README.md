Anagrams
========

For a word of 3 letters such as "CAT".  There are 3! = 3x2x1 = 6 permutations.  Generally, 
if there are n letters there are n! permutations (not considering duplicate letters side-by-side such as "Gee").
Only one letter can hold a position during iterations for n!/n rows.  I'm using the first element to hold which is 
the 0th element of an array.

Example using a word that contains 3 letters ("CAT": array[0]="C", array[1]="A", array[2]="T"), 
holding the 0th element of an array ("C") for every 2 rows a new column:



Index     Letters
0 1 2     C A T
0 2 1     C T A
-----     -----
1 0 2     A C T
2 0 1     T C A
-----     -----
1 2 0     A T C
2 1 0     T A C


Example using a 4 letters word ("ACTG") , holding 0th element of array ("A") for every 6 rows a new column:
Index       Letters
0 1 2 3     A C T G
0 1 3 2     A C G T
0 2 1 3     A T C G
0 3 1 2     A G C T
0 2 3 1     A T G C
0 3 2 1     A G T C
-------     -------
1 0 2 3     C A T G
1 0 3 2     C A G T
2 0 1 3     T A C G
3 0 1 2     G A C T
2 0 3 1     T A G C
3 0 2 1     G A T C
-------     -------
1 2 0 3     C T A G
1 3 0 2     C G A T
2 1 0 3     T C A G
3 1 0 2     G C A T
2 3 0 1     T G A C
3 2 0 1     G T A C
-------     -------
1 2 3 0     C T G A
1 3 2 0     C G T A
2 1 3 0     T C G A 
3 1 2 0     G C T A
2 3 1 0     T G C A
3 2 1 0     G T C A

You might notice a mirror image if you split the rows in half.  This fact could be used for optimization.

