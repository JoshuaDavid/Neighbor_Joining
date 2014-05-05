# This boilerplate is required to include files from the src/ directory of this
# project.
from sys import path
from os.path import realpath, dirname
path.append(realpath(dirname(__file__) + "/../src"))
import unittest
import distancetree

def sortby(indices):
    def sortfn(arr):
        return [x for (y, x) in sorted(zip(indices, arr))]
    return sortfn

class TestNeighborJoining(unittest.TestCase):
    def setUp(self):
        pass
    def test_equal_leaves_are_equal(self):
        a = distancetree.Leaf("leaf")
        b = distancetree.Leaf("leaf")
        self.assertEqual(a, b)
    def test_unequal_leaves_are_unequal(self):
        a = distancetree.Leaf("leaf")
        b = distancetree.Leaf("leaf2")
        self.assertNotEqual(a, b)
    def test_equal_trees_are_equal(self):
        a = distancetree.Leaf("leaf")
        b = distancetree.Leaf("leaf")
        c = distancetree.Tree(a, b)
        d = distancetree.Tree(b, a)
        self.assertEqual(c, d)
    def test_unequal_trees_are_unequal(self):
        a = distancetree.Leaf("leaf")
        b = distancetree.Leaf("leaf2")
        c = distancetree.Tree(a, a)
        d = distancetree.Tree(b, a)
        self.assertNotEqual(c, d)
    def test_trees_with_switched_branches_are_equal(self):
        a = distancetree.Leaf("leaf1")
        b = distancetree.Leaf("leaf2")
        c = distancetree.Tree(a, b)
        d = distancetree.Tree(b, a)
        self.assertEqual(c, d)

if __name__ == '__main__':
    unittest.main()
