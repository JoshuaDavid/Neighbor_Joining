# This boilerplate is required to include files from the src/ directory of this
# project.
from sys import path
from os.path import realpath, dirname
path.append(realpath(dirname(__file__) + "/../src"))
import unittest
import numpy
import numpy_nj
import distancetree
from random import shuffle

class TestCase:
    def __init__(self, dmatrix, leaves):
        self.D = numpy.matrix(dmatrix)
        self.forest = numpy.array(map(distancetree.Leaf, leaves))

def sortby(indices):
    def sortfn(arr):
        return [x for (y, x) in sorted(zip(indices, arr))]
    return sortfn

class TestNeighborJoining(unittest.TestCase):
    def setUp(self):
        pass
    def test_head(self):
        self.assertEqual(numpy_nj.head(range(0, 10)), 0)
    def test_tail(self):
        self.assertEqual(numpy_nj.tail(range(0, 10)), range(1, 10))
    def test_neighborJoin_not_affected_by_shuffle(self):
        testcases = []
        dmatrix = [[0, 5, 4, 7, 6, 8]\
                  ,[5, 0, 7,10, 9,11]\
                  ,[4, 7, 0, 7, 6, 8]\
                  ,[7,10, 7, 0, 5, 9]\
                  ,[6, 9, 6, 5, 0, 8]\
                  ,[8,11, 8, 9, 8, 0]]
        leaves = ['a', 'b', 'c', 'd', 'e', 'f']
        testcases.append(TestCase(dmatrix, leaves))
        newids = range(6)
        shuffle(newids)
        leaves  = sortby(newids)(leaves)
        dmatrix = sortby(newids)(map(sortby(newids), dmatrix))
        testcases.append(TestCase(dmatrix, leaves))
        results = [numpy_nj.neighborJoin(t.D, t.forest) for t in testcases]
        return 



if __name__ == '__main__':
    unittest.main()
