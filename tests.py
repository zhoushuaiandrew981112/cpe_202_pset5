from pset5 import *
import unittest

class Test_pset5(unittest.TestCase):

    """ TreeNode """

    def test_TreeNode_init(self):
        n_5 = TreeNode(5, "five")
        self.assertEqual(n_5.key, 5)
        self.assertEqual(n_5.val, "five")
        self.assertEqual(n_5.parent, None)
        self.assertEqual(n_5.l_child, None)
        self.assertEqual(n_5.r_child, None)


        n_4 = TreeNode(4, "four")
        n_6 = TreeNode(6, "six")
        n_5 = TreeNode(5, "five", None, n_4, n_6)
        self.assertEqual(n_5.key, 5)
        self.assertEqual(n_5.val, "five")
        self.assertEqual(n_5.parent, None)
        self.assertEqual(n_5.l_child, n_4)
        self.assertEqual(n_5.r_child, n_6)

    """ BinarySearchTree """

    def test_BST_init(self):
        bst = BinarySearchTree(5)
        self.assertEqual(bst.key, 5)
        self.assertEqual(bst.val, None)

        bst = BinarySearchTree(5, "five")
        self.assertEqual(bst.key, 5)
        self.assertEqual(bst.val, "five")















if __name__ == "__main__":
    unittest.main()
