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

    def test_has_l_r_child_parernt(self):
        n = TreeNode(1, "one")

        self.assertFalse(n.has_l_child())
        self.assertFalse(n.has_r_child())
        self.assertFalse(n.has_parent())

        n_l = TreeNode(0, "zero")
        n_r = TreeNode(2, "two")
        n_p = TreeNode(3, "three")

        self.assertFalse(n_l.has_parent())
        self.assertFalse(n_r.has_parent())
        self.assertFalse(n_p.has_parent())

        n = TreeNode(1, "one", n_p, n_l, n_r)
        self.assertTrue(n.has_l_child())
        self.assertTrue(n.has_r_child())
        self.assertTrue(n.has_parent())

    """ BinarySearchTree """

    def test_BST_init(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.root, None)
 
        bst = BinarySearchTree(5)
        self.assertEqual(bst.root.key, 5)
        self.assertEqual(bst.root.val, None)

        bst = BinarySearchTree(5, "five")
        self.assertEqual(bst.root.key, 5)
        self.assertEqual(bst.root.val, "five")

    def test_bst_add(self):
        bst = BinarySearchTree()
        bst.insert(5, "five")
        #             5
        #            / \
        #         None None
        self.assertEqual(bst.root.key, 5)
        self.assertEqual(bst.root.val, "five")
        self.assertEqual(bst.root.parent, None)
        self.assertEqual(bst.root.l_child, None)
        self.assertEqual(bst.root.r_child, None)
        self.assertFalse(bst.root.has_l_child())
        self.assertFalse(bst.root.has_r_child())

        bst.insert(4, "four")
        bst.insert(6, "six")
        #             5
        #            / \
        #           4   6
        self.assertTrue(bst.root.has_l_child())
        self.assertTrue(bst.root.has_r_child())

        current_4 = bst.root.l_child   # node 4
        current_6 = bst.root.r_child   # node 6

        self.assertEqual(current_4.key, 4)
        self.assertEqual(current_4.val, "four")
        self.assertEqual(current_4.parent, bst.root)
        self.assertEqual(current_4.l_child, None)
        self.assertEqual(current_4.r_child, None)
        self.assertFalse(current_4.has_l_child())
        self.assertFalse(current_4.has_r_child())

        self.assertEqual(current_6.key, 6)
        self.assertEqual(current_6.val, "six")
        self.assertEqual(current_6.parent, bst.root)
        self.assertEqual(current_6.l_child, None)
        self.assertEqual(current_6.r_child, None)
        self.assertFalse(current_6.has_l_child())
        self.assertFalse(current_6.has_r_child())

        bst.insert(3, "three")
        bst.insert(7, "seven")
        
        #             5
        #            / \
        #           4   6
        #          /     \
        #         3       7
        self.assertTrue(current_4.has_l_child())
        self.assertFalse(current_4.has_r_child())
        self.assertFalse(current_6.has_l_child())
        self.assertTrue(current_6.has_r_child())
        

        current_3 = current_4.l_child  # node 3
        current_7 = current_6.r_child  # node 7

        self.assertEqual(current_3.key, 3)
        self.assertEqual(current_3.val, "three")
        self.assertEqual(current_3.parent, current_4)
        self.assertEqual(current_3.l_child, None)
        self.assertEqual(current_3.r_child, None)
        self.assertFalse(current_3.has_l_child())
        self.assertFalse(current_3.has_r_child())

        self.assertEqual(current_7.key, 7)
        self.assertEqual(current_7.val, "seven")
        self.assertEqual(current_7.parent, current_6)
        self.assertEqual(current_7.l_child, None)
        self.assertEqual(current_7.r_child, None)
        self.assertFalse(current_7.has_l_child())
        self.assertFalse(current_7.has_r_child())

       
        bst = BinarySearchTree()
        bst.insert(7, "seven")
        bst.insert(4, "four")
        bst.insert(10, "ten")
        bst.insert(1, "one")
        bst.insert(6, "six")
        bst.insert(8, "eight")
        bst.insert(12, "twelve")
        bst.insert(0, "zero")
        bst.insert(5, "five")
        bst.insert(9, "nine")
        bst.insert(11, "eleven")
        #              7
        #           /     \
        #          4       10
        #         / \     / \
        #        1   6   8   12
        #       /    /   \   /
        #      0    5     9 11
        current_7 = bst.root
        current_4 = current_7.l_child
        current_10 = current_7.r_child
        current_1 = current_4.l_child
        current_6 = current_4.r_child
        current_8 = current_10.l_child
        current_12 = current_10.r_child
        current_0 = current_1.l_child
        current_5 = current_6.l_child
        current_9 = current_8.r_child
        current_11 = current_12.l_child

        self.assertEqual(current_7.key, 7)
        self.assertEqual(current_4.key, 4)
        self.assertEqual(current_10.key, 10)
        self.assertEqual(current_1.key, 1)
        self.assertEqual(current_6.key, 6)
        self.assertEqual(current_8.key, 8)
        self.assertEqual(current_12.key, 12)
        self.assertEqual(current_0.key, 0)
        self.assertEqual(current_5.key, 5)
        self.assertEqual(current_9.key, 9)
        self.assertEqual(current_11.key, 11)

        self.assertEqual(current_7.val, "seven")
        self.assertEqual(current_4.val, "four")
        self.assertEqual(current_10.val, "ten")
        self.assertEqual(current_1.val, "one")
        self.assertEqual(current_6.val, "six")
        self.assertEqual(current_8.val, "eight")
        self.assertEqual(current_12.val, "twelve")
        self.assertEqual(current_0.val, "zero")
        self.assertEqual(current_5.val, "five")
        self.assertEqual(current_9.val, "nine")
        self.assertEqual(current_11.val, "eleven")


    def test_contains_helper(self):
        bst = BinarySearchTree()
        bst.insert(5, "five")
        bst.insert(4, "four")
        bst.insert(6, "six")
        bst.insert(3, "three")
        bst.insert(7, "seven")
        #             5
        #            / \
        #           4   6
        #          /     \
        #         3       7
               










if __name__ == "__main__":
    unittest.main()
