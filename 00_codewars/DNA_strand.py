# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
import unittest

def DNA_strand(dna):
  return dna.replace('A', 't').replace('T', 'A').replace('t', 'T').replace('C', 'g').replace('G', 'C').replace('g', 'G')


# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")