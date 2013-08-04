Pysuffix with utility functions
========

Implementation of suffix array (similar function as suffix tree, see wikipedia) in python, derived from 
https://code.google.com/p/pysuffix/

Utility function is added to show simple application of searching substring and finding longest repeating substring.

Usage
========

    s = 'aaaabcaa'
    occurance = search('aa', s)
    self.assertEquals(occurance, [0, 1, 2, 6])