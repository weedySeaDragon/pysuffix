Pysuffix with utility functions
========

Implementation of suffix array (similar function as suffix tree, see wikipedia) in python, derived from 
https://code.google.com/p/pysuffix/

Utility function is added to show simple application of searching substring and finding longest repeating substring.

Usage
========
    import suffixArrayApplications as saApp
    s = 'aaaabcaa'
    occurance = saApp.search('aa', s)
    self.assertEquals(occurance, [0, 1, 2, 6])