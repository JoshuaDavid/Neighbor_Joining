# This boilerplate is required to include files from the src/ directory of this
# project.
from sys import path
from os.path import realpath, dirname
path.append(realpath(dirname(__file__) + "/../src"))
import unittest
from distancetree import Tree, Leaf

def sortby(indices):
    def sortfn(arr):
        return [x for (y, x) in sorted(zip(indices, arr))]
    return sortfn

class TestNeighborJoining(unittest.TestCase):
    def setUp(self):
        self.ab_cd = Tree(Tree(Leaf("a"), Leaf("b")), Tree(Leaf("c"), Leaf("d")))
        self.ab = self.ab_cd.left
        self.cd = self.ab_cd.right
        self.a = self.ab.left
        self.b = self.ab.right
        self.c = self.cd.left
        self.d = self.cd.right
        pass
    def test_equal_leaves_are_equal(self):
        self.assertEqual(self.a, self.a)
    def test_unequal_leaves_are_unequal(self):
        self.assertNotEqual(self.a, self.b)
    def test_equal_trees_are_equal(self):
        self.assertEqual(self.ab, self.ab)
    def test_unequal_trees_are_unequal(self):
        aa = Tree(self.a, self.a)
        self.assertNotEqual(aa, self.ab)
    def test_trees_with_switched_branches_are_equal(self):
        cd_ba = Tree(self.cd, Tree(self.b, self.a))
        self.assertEqual(self.ab_cd, cd_ba)
    def test_tree_contains_self(self):
        self.assertTrue(self.ab_cd.contains(self.ab_cd))
    def test_tree_contains_all_subtrees(self):
        ab_c = Tree(self.ab, self.c)
        self.assertTrue(ab_c.contains(ab_c.left))
        self.assertTrue(ab_c.contains(ab_c.right))
    def test_tree_contains_all_leaves(self):
        self.assertTrue(self.ab_cd.contains(self.a))
        self.assertTrue(self.ab_cd.contains(self.b))
        self.assertTrue(self.ab_cd.contains(self.c))
        self.assertTrue(self.ab_cd.contains(self.d))
    def test_distanceTo(self):
        self.assertEqual(2, self.a.distanceTo(self.b))
        self.assertEqual(2, self.c.distanceTo(self.d))
        self.assertEqual(4, self.a.distanceTo(self.d))
    def test_distanceTo_raises_error_if_unreachable(self):
        e = Leaf("e")
        self.assertRaises(LookupError, self.a.distanceTo, e)

if __name__ == '__main__':
    unittest.main()
