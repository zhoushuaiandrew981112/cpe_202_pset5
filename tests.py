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

    def test_is_l_r_child_and_is_leaf(self):

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

        self.assertTrue(current_4.is_l_child())
        self.assertTrue(current_10.is_r_child())
        self.assertTrue(current_1.is_l_child())
        self.assertTrue(current_6.is_r_child())
        self.assertTrue(current_8.is_l_child())
        self.assertTrue(current_12.is_r_child())
        self.assertTrue(current_0.is_l_child())
        self.assertTrue(current_9.is_r_child())
        self.assertTrue(current_5.is_l_child())
        self.assertTrue(current_11.is_l_child())
        self.assertFalse(current_7.is_l_child())
        self.assertFalse(current_7.is_r_child())

        self.assertTrue(current_0.is_leaf())
        self.assertTrue(current_5.is_leaf())
        self.assertTrue(current_9.is_leaf())
        self.assertTrue(current_11.is_leaf())
        self.assertFalse(current_7.is_leaf())
        self.assertFalse(current_4.is_leaf())
        self.assertFalse(current_10.is_leaf())

    def test_has_one_child(self):

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

        self.assertTrue(current_1.has_one_child())
        self.assertTrue(current_6.has_one_child())
        self.assertTrue(current_8.has_one_child())
        self.assertTrue(current_12.has_one_child())

        self.assertFalse(current_7.has_one_child())
        self.assertFalse(current_4.has_one_child())
        self.assertFalse(current_10.has_one_child())
        self.assertFalse(current_0.has_one_child())
        self.assertFalse(current_5.has_one_child())
        self.assertFalse(current_9.has_one_child())
        self.assertFalse(current_11.has_one_child())

    def test_replace_node_data(self):
        n_l = TreeNode(0, "zero")
        n_r = TreeNode(5, "five")
        n_p = TreeNode(4, "four")
        n_t = TreeNode(3, "three",n_p ,n_l, n_r)

        new_n_l = TreeNode(1, "one")
        new_n_r = TreeNode(6, "six")
        n_t.replace_node_data(10, "ten", new_n_l, new_n_r)

        self.assertEqual(n_t.key, 10)
        self.assertEqual(n_t.val, "ten")
        self.assertEqual(n_t.l_child, new_n_l)
        self.assertEqual(n_t.r_child, new_n_r)

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

        self.assertTrue(current_7.has_l_child())
        self.assertTrue(current_7.has_r_child())
        self.assertTrue(current_4.has_l_child())
        self.assertTrue(current_4.has_r_child())
        self.assertTrue(current_10.has_l_child())
        self.assertTrue(current_10.has_r_child())
        self.assertTrue(current_1.has_l_child())
        self.assertFalse(current_1.has_r_child())
        self.assertTrue(current_6.has_l_child())
        self.assertFalse(current_6.has_r_child())
        self.assertFalse(current_8.has_l_child())
        self.assertTrue(current_8.has_r_child())
        self.assertTrue(current_12.has_l_child())
        self.assertFalse(current_12.has_r_child())
        self.assertFalse(current_0.has_l_child())
        self.assertFalse(current_0.has_r_child())
        self.assertFalse(current_5.has_l_child())
        self.assertFalse(current_5.has_r_child())
        self.assertFalse(current_9.has_l_child())
        self.assertFalse(current_9.has_r_child())
        self.assertFalse(current_11.has_l_child())
        self.assertFalse(current_11.has_r_child())

    def test_contains_helper(self):
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
        
        act_bool = bst.contains_helper(current_7, 7)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_4, 4)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_10, 10)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_1, 1)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_6, 6)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_8, 8)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_12, 12)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_0, 0)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_5, 5)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_9, 9)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_11, 11)
        self.assertTrue(act_bool)
        act_bool = bst.contains_helper(current_7, 100)
        self.assertFalse(act_bool)

        act_bool = bst.contains(7)
        self.assertTrue(act_bool)
        act_bool = bst.contains(4)
        self.assertTrue(act_bool)
        act_bool = bst.contains(10)
        self.assertTrue(act_bool)
        act_bool = bst.contains(1)
        self.assertTrue(act_bool)
        act_bool = bst.contains(6)
        self.assertTrue(act_bool)
        act_bool = bst.contains(8)
        self.assertTrue(act_bool)
        act_bool = bst.contains(12)
        self.assertTrue(act_bool)
        act_bool = bst.contains(0)
        self.assertTrue(act_bool)
        act_bool = bst.contains(5)
        self.assertTrue(act_bool)
        act_bool = bst.contains(9)
        self.assertTrue(act_bool)
        act_bool = bst.contains(11)
        self.assertTrue(act_bool)
        act_bool = bst.contains(100)
        self.assertFalse(act_bool)
        
    def test_find_min_max(self):
        bst = BinarySearchTree()
        bst.insert(7, "seven")

        self.assertEqual(bst.find_max().key, 7)
        self.assertEqual(bst.find_max().val, "seven")

        bst.insert(4, "four")
        bst.insert(10, "ten")


        self.assertEqual(bst.find_min().key, 4)
        self.assertEqual(bst.find_min().val, "four")
        self.assertEqual(bst.find_max().key, 10)
        self.assertEqual(bst.find_max().val, "ten")

        bst.insert(1, "one")
        bst.insert(6, "six")
        bst.insert(8, "eight")

        self.assertEqual(bst.find_min().key, 1)
        self.assertEqual(bst.find_min().val, "one")

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

        self.assertEqual(bst.find_min().key, 0)
        self.assertEqual(bst.find_min().val, "zero")
        self.assertEqual(bst.find_max().key, 12)
        self.assertEqual(bst.find_max().val, "twelve")
        

    def test_in_pre_post_order_list(self):
        bst = BinarySearchTree()
        bst.insert(7, "seven")
        bst.insert(4, "four")

        act_inorder_lst = bst.inorder_list()
        exp_inorder_lst = [4, 7]
        self.assertEqual(act_inorder_lst, exp_inorder_lst)

        act_preorder_lst = bst.preorder_list()
        exp_preorder_lst = [7, 4]
        self.assertEqual(act_preorder_lst, exp_preorder_lst)

        act_postorder_lst = bst.postorder_list()
        exp_postorder_lst = [4, 7]
        self.assertEqual(act_postorder_lst, exp_postorder_lst)

        bst.insert(10, "ten")
        bst.insert(1, "one")
        bst.insert(6, "six")
        bst.insert(8, "eight")
        bst.insert(12, "twelve")

        act_inorder_lst = bst.inorder_list()
        exp_inorder_lst = [1, 4, 6, 7, 8, 10, 12]
        self.assertEqual(act_inorder_lst, exp_inorder_lst)

        act_preorder_lst = bst.preorder_list()
        exp_preorder_lst = [7, 4, 1, 6, 10, 8, 12]
        self.assertEqual(act_preorder_lst, exp_preorder_lst)

        act_postorder_lst = bst.postorder_list()
        exp_postorder_lst = [1, 6, 4, 8, 12, 10, 7]
        self.assertEqual(act_postorder_lst, exp_postorder_lst)

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

        act_inorder_lst = bst.inorder_list()
        exp_inorder_lst = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(act_inorder_lst, exp_inorder_lst)

        act_preorder_lst = bst.preorder_list()
        exp_preorder_lst = [7, 4, 1, 0, 6, 5, 10, 8, 9, 12, 11]
        self.assertEqual(act_preorder_lst, exp_preorder_lst)

        act_postorder_lst = bst.postorder_list()
        exp_postorder_lst = [0, 1, 5, 6, 4, 9, 8, 11, 12, 10, 7]
        self.assertEqual(act_postorder_lst, exp_postorder_lst)

    def test_delete(self):
        bst = BinarySearchTree()

        found_node = bst.get(bst.root, 0)
        self.assertEqual(found_node, None)
        
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

        found_node = bst.get(bst.root, 0)
        self.assertEqual(found_node.key, 0)
        self.assertEqual(found_node.val, "zero")

        found_node = bst.get(bst.root, 11)
        self.assertEqual(found_node.key, 11)
        self.assertEqual(found_node.val, "eleven")

        found_node = bst.get(bst.root, 4)
        self.assertEqual(found_node.key, 4)
        self.assertEqual(found_node.val, "four")

        # test delet when the target node is leaf
        bst.delete(0)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(0))
        bst.delete(5)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(5))
        bst.delete(9)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(9))
        bst.delete(11)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(11))
        bst.delete(1)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(1))
        bst.delete(6)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(6))
        bst.delete(8)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(8))
        bst.delete(12)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(12))
        bst.delete(4)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(4))
        bst.delete(10)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(10))
        bst.delete(7)
        self.assertEqual(current_1.l_child, None)
        self.assertFalse(bst.contains(7))
        self.assertEqual(bst.root, None)


        # test when the target node has one child
          
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

        bst.delete(1)
        self.assertEqual(current_4.l_child.key, 0)
        bst.delete(6)
        self.assertEqual(current_4.r_child.key, 5)
        bst.delete(8)
        self.assertEqual(current_10.l_child.key, 9)
        bst.delete(12)
        self.assertEqual(current_10.r_child.key, 11)

        # test when the target node has two children

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
        
        


if __name__ == "__main__":
    unittest.main()
