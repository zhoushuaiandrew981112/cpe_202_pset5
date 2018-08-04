# Name:         Zhoushuai (Andrew) Wu
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Pset 5: Binary Search Tree
# Term:         Summer 2018


class TreeNode:

    def __init__(self, key, val = None, parent = None, \
        l_child = None, r_child = None):
        self.key = key
        self.val = val
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child


    def has_parent(self):
        return self.parent != None


    def has_l_child(self):
        return self.l_child != None


    def has_r_child(self):
        return self.r_child != None


class BinarySearchTree:

    def __init__(self, key = None, val = None):
        if key == None:
            self.root = None
        else:
            self.root = TreeNode(key, val)


    def insert_helper(self, key, val, current):
        if key <= current.key:
            if current.has_l_child():
                self.insert_helper(key, val, current.l_child)
            else:
                current.l_child = TreeNode(key, val, current)
        elif key > current.key:
            if current.has_r_child():
                self.insert_helper(key, val, current.r_child)
            else:
                current.r_child = TreeNode(key, val, current) 


    def insert(self, key, val):
        if self.root == None:
            self.root = TreeNode(key, val)
        else:
            self.insert_helper(key, val, self.root)
        

    def delete(self):
        pass

    
    def contains_helper(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return True
        elif node.key < key:
            return contains_helper(node.r_child, key)
        elif node.key > key:
            return contains_helper(node.l_child, key)


    def contains(self, key):
        node = self.root
        return contains_helper(self, node, key)






